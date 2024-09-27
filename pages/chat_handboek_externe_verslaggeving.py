import streamlit as st

st.title("Chat met Handboek Externe verslaggeving")
prompt = st.chat_input("Stel je vraag")
if prompt:
    st.write("**Gebruiker**")
    st.write(f"{prompt}")
    st.write(f"**Antwoord**")
    st.write(f"Lorem ipsum")
    st.write(f"**Bronverwijzing**")
    st.write(f"Lorem ipsum")