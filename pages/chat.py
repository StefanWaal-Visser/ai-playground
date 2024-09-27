import streamlit as st
import time

st.title("Chat met Handboek Externe verslaggeving")
prompt = st.chat_input("Stel je vraag")
if prompt:
    st.write("**Gebruiker**")
    st.write(f"{prompt}")
    st.write("**Antwoord**")
    answer = st.empty()
    answer.text("Laden...")
    st.write("**Bronverwijzing**")
    sources = st.empty()
    sources.text("Laden...")
    time.sleep(1)
    answer.text("Gereed")
    sources.text("Gereed")