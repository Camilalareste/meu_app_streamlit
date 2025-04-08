mport streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
from datetime import datetime
import requests

# Configuração da página
st.set_page_config(page_title="Transporte Inteligente", layout="wide")

# Título principal
st.title("\U0001F6A6 Plataforma de Mobilidade Urbana Inteligente")

# Sidebar: modo de visualização e menu principal
modo = st.sidebar.radio("\U0001F464 Modo de Visualização", ["Usuário", "Gestor"])
aba = st.sidebar.radio("Menu Principal", (
    "Mapa Interativo",
    "Ocorrências 156",
    "Chamados SEDEC",
    "Infraestrutura e Serviços",
    "Chatbot"
))

# Base de localização (Recife)
latitude_base = -8.0476
longitude_base = -34.8770

# Função: Dados simulados de ônibus
def gerar_onibus():
    return [
        {"linha": "101", "lat": latitude_base + random.uniform(-0.01, 0.01), "lon": longitude_base + random.uniform(-0.01, 0.01)},
        {"linha": "102", "lat": latitude_base + random.uniform(-0.01, 0.01), "lon": longitude_base + random.uniform(-0.01, 0.01)},
        {"linha": "103", "lat": latitude_base + random.uniform(-0.01, 0.01), "lon": longitude_base + random.uniform(-0.01, 0.01)}
    ]

# Aba: Mapa Interativo
if aba == "Mapa Interativo":
    st.subheader("\U0001F4CD Mapa em Tempo Real")
    m = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
    for onibus in gerar_onibus():
        folium.Marker([
            onibus["lat"], onibus["lon"]
        ], popup=f"Linha {onibus['linha']}", icon=folium.Icon(color="blue", icon="bus", prefix="fa")).add_to(m)
    folium_static(m)

# Aba: Ocorrências 156
elif aba == "Ocorrências 156":
    st.subheader("\U0001F4CB Solicitações 156 em Tempo Real")
    resource_id = "9afa68cf-7fd9-4735-b157-e23da873fef7"
    api_url = f"https://dados.recife.pe.gov.br/api/3/action/datastore_search?resource_id={resource_id}&limit=100"

    try:
        response = requests.get(api_url)
        data = response.json()
        if data.get("success"):
            df = pd.DataFrame(data["result"]["records"])
            st.success("\u2705 Dados 156 carregados com sucesso da API!")
            st.dataframe(df)
        else:
            st.error("\u274C Erro ao acessar a API CKAN.")
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")

# Aba: Chamados SEDEC
elif aba == "Chamados SEDEC":
    st.subheader("\U0001F4CA Chamados SEDEC (em construção)")
    st.info("Este módulo está em desenvolvimento.")

# Aba: Infraestrutura e Serviços
elif aba == "Infraestrutura e Serviços":
    st.subheader("\U0001F3D7\ufe0f Infraestrutura Urbana")
    st.info("Em breve: dados de câmeras, fiscalização e estruturas viárias.")

# Aba: Chatbot
elif aba == "Chatbot":
    st.subheader("\U0001F916 Assistente Virtual")
    st.markdown("Chatbot será integrado para tirar dúvidas sobre mobilidade urbana.")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Camila Lareste • Dados: Prefeitura do Recife • v1.0")

