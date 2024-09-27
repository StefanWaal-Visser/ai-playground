import streamlit as st

def main():
    # builds the sidebar menu
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Individual Checker')
        st.page_link('pages/chat_handboek_externe_verslaggeving.py', label='Chat met handboek externe verslaggeving')

    st.title("Welkom bij de Visser & Visser AI Playground")
    st.write(
    """In deze omgeving zijn verschillende AI modules beschikbaar die door het team IT, Data & Innovatie is ontwikkeld. De modules worden allemaal in Bèta versie vrijgegeven. 
    Houdt rekening met instabiliteit en onverwachte uitkomsten.
    Wij nodigen iedere gebruiker van harte uit alle opbouwende feedback te delen.
    Mail alle opmerkingen, vragen en complimenten naar diu@visser-visser.nl.""")


if __name__ == '__main__':
    main()
