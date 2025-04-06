streamlit_app.py
import streamlit as st

st.set_page_config(page_title="Conteúdo dos Documentos", layout="wide")

st.title("📄 Visualizador de Documentos")

st.header("📘 Documento 1: Redução de Custos na Frota")
st.markdown("""
*Aqui entra o conteúdo do primeiro documento que você me mandou. Você pode copiar e colar aqui o texto.*
""")

st.header("📗 Documento 2: Tendências em Transporte")
st.markdown("""
*Aqui entra o conteúdo do segundo documento.*
""")

st.header("📙 Documento 3: Boas Práticas na Logística")
st.markdown("""
*Aqui entra o conteúdo do terceiro documento.*
""")

