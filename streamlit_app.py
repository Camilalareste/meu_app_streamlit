import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from datetime import datetime
import random

st.set_page_config(page_title="Transporte Inteligente", layout="wide")

st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")
st.markdown("Aplicativo para visualização de dados de mobilidade urbana e serviços públicos em tempo real no Recife.")

# Sidebar
modo = st.sidebar.radio("👤 Modo de Visualização", ["Usuário", "Gestor"])
st.sidebar.markdown("Veja informações úteis de transporte ao seu redor.")
aba = st.sidebar.radio("Navegação", ("Mapa Interativo", "Dados 156", "Chamados SEDEC", "Chatbot"))

# Localização base Recife
latitude_base = -8.0476
longitude_base = -34.8770

# Função para gerar posições próximas
def gerar_posicao_proxima(base_lat, base_lon, variacao=0.01):
    return base_lat + random.uniform(-variacao, variacao), base_lon + random.uniform(-variacao, variacao)

# Aba Mapa Interativo
if aba == "Mapa Interativo":
    st.subheader("🗺️ Mapa Interativo de Ocorrências e Serviços")

    # Criar mapa
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

    # Marcar pontos aleatórios
    for _ in range(15):
        lat, lon = gerar_posicao_proxima(latitude_base, longitude_base)
        folium.Marker(
            location=[lat, lon],
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(mapa)

    folium_static(mapa)

# Aba Dados 156
elif aba == "Dados 156":
    st.subheader("📞 Dados do Sistema 156")
    st.write("Dados fictícios para ilustração.")
    dados_156 = pd.DataFrame({
        "Categoria": ["Buraco na via", "Iluminação pública", "Coleta de lixo"],
        "Quantidade": [123, 98, 76]
    })
    st.dataframe(dados_156)

# Aba Chamados SEDEC
elif aba == "Chamados SEDEC":
    st.subheader("🚨 Chamados SEDEC")
    st.write("Informações simuladas dos chamados de emergência.")
    chamados = pd.DataFrame({
        "Ocorrência": ["Alagamento", "Deslizamento", "Queda de árvore"],
        "Bairro": ["Boa Viagem", "Tamarineira", "Casa Forte"],
        "Status": ["Resolvido", "Em andamento", "Pendente"]
    })
    st.dataframe(chamados)

# Aba Chatbot
elif aba == "Chatbot":
    st.subheader("🤖 Chatbot")
    st.info("Esta funcionalidade está em desenvolvimento.")
