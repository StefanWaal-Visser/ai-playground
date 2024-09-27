import streamlit as st

pg = st.navigation([
    st.Page("pages/home.py", title="Startpagina"),
    st.Page("pages/chat.py", title="Chat met Handboek Externe verslaggeving")])
pg.run()
