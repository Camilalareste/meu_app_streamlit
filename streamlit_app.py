import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
from datetime import datetime
import requests
from folium.plugins import MarkerCluster

# Configuração da página
st.set_page_config(page_title="Transporte Inteligente", layout="wide")

# Título principal
st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Sidebar: modo de visualização e menu principal
modo = st.sidebar.radio("👤 Modo de Visualização", ["Usuário", "Gestor"])
aba = st.sidebar.radio("Menu Principal", (
    "Mapa Interativo",
    "Ocorrências 156",
    "Chamados SEDEC",
    "Infraestrutura e Serviços",
    "Chatbot"
))

# Coordenadas base (Recife)
latitude_base = -8.0476
longitude_base = -34.8770

# Função para adicionar ícones personalizados
def adicionar_icones(mapa):
    icones = [
        {"tipo": "Lixo", "icone": "trash", "cor": "green"},
        {"tipo": "Trânsito", "icone": "car", "cor": "red"},
        {"tipo": "Metrô", "icone": "train", "cor": "purple"},
        {"tipo": "Zona Azul", "icone": "info-sign", "cor": "blue"},
        {"tipo": "Acidente", "icone": "exclamation-sign", "cor": "orange"},
    ]
    for i in range(15):
        icone = random.choice(icones)
        lat_offset = random.uniform(-0.01, 0.01)
        lon_offset = random.uniform(-0.01, 0.01)
        folium.Marker(
            location=[latitude_base + lat_offset, longitude_base + lon_offset],
            popup=f"{icone['tipo']} #{i+1}",
            icon=folium.Icon(color=icone['cor'], icon=icone['icone'], prefix='glyphicon')
        ).add_to(mapa)

# Função para carregar dados da API CKAN
@st.cache_data
def carregar_dados_156():
    url_api = "http://dados.recife.pe.gov.br/api/3/action/datastore_search"
    resource_id = "9afa68cf-7fd9-4735-b157-e23da873fef7"  # ID do recurso CSV 156
    try:
        resposta = requests.get(url_api, params={"resource_id": resource_id, "limit": 100})
        dados = resposta.json()["result"]["records"]
        return pd.DataFrame(dados)
    except Exception as e:
        st.error(f"Erro ao carregar dados 156: {e}")
        return pd.DataFrame()

# Mapa Interativo
if aba == "Mapa Interativo":
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
    adicionar_icones(mapa)
    folium_static(mapa)

# Ocorrências 156
elif aba == "Ocorrências 156":
    st.subheader("📋 Solicitações 156 em Tempo Real")
    df_156 = carregar_dados_156()
    if not df_156.empty:
        st.success("✅ Dados 156 carregados com sucesso da API!")
        st.dataframe(df_156.head(50))
    else:
        st.warning("⚠️ Nenhum dado encontrado.")

# Chamados SEDEC
elif aba == "Chamados SEDEC":
    st.subheader("🆘 Chamados da Defesa Civil (SEDEC)")
    st.info("🔧 Em breve integração com dados de chamados da Defesa Civil")

# Infraestrutura e Serviços
elif aba == "Infraestrutura e Serviços":
    st.subheader("🏗️ Monitoramento de Infraestrutura Urbana")
    st.info("📡 Módulo em desenvolvimento com dados sobre semáforos, câmeras e sensores")

# Chatbot
elif aba == "Chatbot":
    st.subheader("🤖 Chatbot Inteligente para Dúvidas sobre Mobilidade")
    st.info("💬 Em breve integração com modelo conversacional para responder dúvidas do cidadão.")
