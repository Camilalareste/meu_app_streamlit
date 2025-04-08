import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
from datetime import datetime
import requests
from folium.plugins import MarkerCluster

# aba = st.sidebar.radio("Menu Principal", (
    "Mapa Interativo",
    "Ocorrências 156",
    "Chamados SEDEC",
    "Infraestrutura e Serviços",
    "Chatbot",
    "🔍 Análises Inteligentes (IA)"

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

# Função para criar mapa interativo com pontos simulados
def criar_mapa():
    mapa = folium.Map(location=[-8.0476, -34.8770], zoom_start=12)  # Recife
    marcador_cluster = MarkerCluster().add_to(mapa)

    # Simulando dados aleatórios
    for _ in range(50):
        lat = -8.0476 + random.uniform(-0.05, 0.05)
        lon = -34.8770 + random.uniform(-0.05, 0.05)
        folium.Marker(
            location=[lat, lon],
            popup=f"Ocorrência: {random.choice(['Acidente', 'Obra', 'Congestionamento'])}",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(marcador_cluster)

    return mapa

# Aba: Mapa Interativo
if aba == "Mapa Interativo":
    st.subheader("📍 Visualização Interativa de Ocorrências")
    mapa = criar_mapa()
    folium_static(mapa, width=1200, height=600)

# Outras abas: placeholders por enquanto
elif aba == "Ocorrências 156":
    st.subheader("📞 Ocorrências registradas via 156")
    st.info("Em breve: Dados reais de ocorrências 156 serão exibidos aqui.")

elif aba == "Chamados SEDEC":
    st.subheader("🚨 Chamados da Defesa Civil (SEDEC)")
    st.info("Em breve: Visualização de chamados da SEDEC integrados.")

elif aba == "Infraestrutura e Serviços":
    st.subheader("🛣️ Infraestrutura e Serviços de Mobilidade")
    st.info("Em breve: Informações sobre semáforos, câmeras e sinalização.")

elif aba == "Chatbot":
    st.subheader("🤖 Chatbot de Mobilidade")
    st.info("Em breve: Assistente virtual para dúvidas e sugestões.")


if aba == "Rotas e Informações em Tempo Real":
    st.subheader("🚶‍♀️ Rotas e Situações em Tempo Real")

    # Criação do mapa com base em localização central (Recife)
    mapa_usuario = folium.Map(location=[-8.0476, -34.8770], zoom_start=13)

    # Pontos simulados (paradas, acidentes, obras etc.)
    folium.Marker([-8.05, -34.88], tooltip="Parada de ônibus - Linha 101", icon=folium.Icon(color="blue", icon="bus", prefix='fa')).add_to(mapa_usuario)
    folium.Marker([-8.04, -34.875], tooltip="Obra - Interdição parcial", icon=folium.Icon(color="orange", icon="wrench", prefix='fa')).add_to(mapa_usuario)
    folium.Marker([-8.045, -34.873], tooltip="Zona Azul disponível", icon=folium.Icon(color="green", icon="car", prefix='fa')).add_to(mapa_usuario)
    folium.Marker([-8.043, -34.872], tooltip="Acidente recente", icon=folium.Icon(color="red", icon="exclamation-triangle", prefix='fa')).add_to(mapa_usuario)



    import streamlit as st
import folium
from streamlit_folium import folium_static
import random
from datetime import datetime

# Configurações da página
st.set_page_config(page_title="Plataforma de Mobilidade", layout="wide")
st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Menu lateral
aba = st.sidebar.radio("Menu Principal", (
    "Rotas e Informações em Tempo Real",
    "Ocorrências 156",
    "Chamados SEDEC",
    "Infraestrutura e Serviços",
    "Chatbot"
))

# Simulador de dados em tempo real (hipotético)
if aba == "Rotas e Informações em Tempo Real":
    st.header("📍 Situação em Tempo Real")

    # Localização base
    latitude_base = -8.0476
    longitude_base = -34.8770
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

    # Exemplo de ocorrências no mapa
    ocorrencias = [
        {"tipo": "Acidente", "lat": -8.045, "lon": -34.875, "descricao": "Colisão leve"},
        {"tipo": "Obra", "lat": -8.050, "lon": -34.880, "descricao": "Recapeamento asfáltico"},
        {"tipo": "Zona Azul", "lat": -8.048, "lon": -34.870, "descricao": "Estacionamento disponível"},
        {"tipo": "Alagamento", "lat": -8.052, "lon": -34.882, "descricao": "Ponto de alagamento ativo"},
        {"tipo": "Fiscalização", "lat": -8.049, "lon": -34.878, "descricao": "Blitz em andamento"}
    ]

    # Ícones personalizados por tipo
    icones = {
        "Acidente": "🚗",
        "Obra": "🚧",
        "Zona Azul": "🅿️",
        "Alagamento": "🌧️",
        "Fiscalização": "👮"
    }

    for o in ocorrencias:
        folium.Marker(
            location=[o["lat"], o["lon"]],
            popup=f'{icones[o["tipo"]]} {o["tipo"]}: {o["descricao"]}',
            tooltip=o["tipo"],
            icon=folium.Icon(color="blue" if o["tipo"] == "Zona Azul" else "red")
        ).add_to(mapa)

    folium_static(mapa)

    st.subheader("ℹ️ Dicas baseadas nos dados")
    st.markdown("""
    - Evite a Av. X por causa de um acidente.
    - Estacionamentos Zona Azul disponíveis na Rua Y.
    - Alerta de alagamento na região do bairro Z.
    - Tempo estimado até o centro: **32 minutos**.
    """)



    st.markdown("### 🗺️ Mapa da cidade com eventos em tempo real")
    folium_static(mapa_usuario)

    st.markdown("Você também pode **reportar uma ocorrência** ou verificar **rotas alternativas** em breve.")


