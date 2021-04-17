import streamlit as st

def sidebar(PAGES:dict):
    st.sidebar.image(
        'https://media-exp1.licdn.com/dms/image/C4E0BAQGS2T9koVZkjA/company-logo_200_200/0/1579130321928?e=2159024400&v=beta&t=AcfdLGws3IJ43Dn9DLL8nOzly96glVqsQuY0ukYlAig'
    )
    st.sidebar.title("Bienvenido")
    selection=st.sidebar.radio("Ir a:", list(PAGES.keys()))
    return selection
