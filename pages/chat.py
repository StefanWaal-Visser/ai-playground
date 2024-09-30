import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import os
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY'] = ""

PROMPT_TEMPLATE = """
Beantwoord de vraag op basis van alleen de volgende context:

{context}

---

Beantwoord de vraag op basis van de bovenstaande context: {question}
"""

@st.cache_data
def get_pages():
    loader = PyPDFLoader("data/deloitte-nl-audit-handboek-externe-verslaggeving-2023.pdf")
    pages = []
    for page in loader.lazy_load():
        pages.append(page)
    return pages

@st.cache_data
def get_chunks():
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=150,
        length_function=len,
        add_start_index=True,
    )
    pages = get_pages()
    return text_splitter.split_documents(pages)

def get_vector_store():
    chunks = get_chunks()
    return InMemoryVectorStore.from_documents(chunks, OpenAIEmbeddings())

st.title("Chat met Handboek Externe verslaggeving")
prompt = st.chat_input("Stel je vraag")
if prompt:
    st.write("**Gebruiker**")
    st.write(f"{prompt}")
    st.write("**Antwoord**")
    answer_block = st.empty()
    answer_block.text("Laden...")
    st.write("**Bronverwijzing**")
    sources_block = st.empty()
    sources_block.text("Laden...")
    # Set up vector store
    vector_store = get_vector_store()
    sources = vector_store.similarity_search(prompt, k=2)
    # Extract the sources
    sources_text = ""
    for source in sources:
        sources_text += f"{source.metadata['source']} pagina {source.metadata['page']}\n\n"
        sources_text += source.page_content
        sources_text += "\n\n"
    sources_block.text(sources_text)

    # Put the sources in the prompt
    context_text = "\n\n---\n\n".join([source.page_content for source in sources])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=prompt)

    # Ask ChatGPT the question
    response = ChatOpenAI().invoke(prompt)
    answer_block.text(response.content)
    