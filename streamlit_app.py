import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from datetime import datetime
import openai

st.set_page_config(page_title="Transporte Inteligente", layout="wide")

# Cabeçalho
st.title("📊 Transporte Inteligente - Dados em Tempo Real")
st.markdown("Aplicativo para visualização de dados de mobilidade urbana e serviços públicos em tempo real no Recife.")

# Layout com abas
aba = st.sidebar.radio("Escolha uma opção:", ("Mapa Interativo", "Dados 156", "Chamados SEDEC", "Chatbot"))

# Dados (você pode atualizar esses caminhos ou URLs)
@st.cache_data
def carregar_dados():
    dados_156 = pd.read_csv("156_cco_diario.csv", sep=";")
    sedec = pd.read_csv("sedec_chamados_tempo_real.csv", sep=";")
    return dados_156, sedec

dados_156, sedec = carregar_dados()

if aba == "Mapa Interativo":
    st.header("🗺️ Mapa Interativo - Chamados SEDEC")
    
    mapa = folium.Map(location=[-8.0476, -34.8770], zoom_start=12)
    
    for _, row in sedec.iterrows():
        if pd.notna(row.get("LAT")) and pd.notna(row.get("LNG")):
            folium.CircleMarker(
                location=[row["LAT"], row["LNG"]],
                radius=4,
                color="blue",
                fill=True,
                fill_opacity=0.6,
                popup=f"{row.get('SERVICO', '')} - {row.get('BAIRRO', '')}"
            ).add_to(mapa)
    
    folium_static(mapa)

elif aba == "Dados 156":
    st.header("📄 Dados de Solicitações 156")
    st.dataframe(dados_156)

elif aba == "Chamados SEDEC":
    st.header("🚨 Chamados da Defesa Civil (SEDEC)")
    st.dataframe(sedec)

elif aba == "Chatbot":
    st.header("🤖 Assistente IA - Mobilidade Urbana")
    pergunta = st.text_input("Digite sua pergunta sobre os dados:")

    if pergunta:
        openai.api_key = st.secrets["OPENAI_API_KEY"]
        with st.spinner("Analisando com IA..."):
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente que analisa dados de mobilidade urbana do Recife."},
                    {"role": "user", "content": pergunta}
                ]
            )
            st.success(resposta.choices[0].message["content"])


