import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
import requests
from folium.plugins import MarkerCluster

# Page Configuration
st.set_page_config(page_title="Plataforma de Mobilidade Urbana", layout="wide")

# Title
st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Sidebar: View Mode and Main Menu
modo = st.sidebar.radio("👤 Modo de Visualização", ["Usuário", "Gestor"])
aba = st.sidebar.radio("Menu Principal", (
    "Mapa Interativo",
    "Ocorrências 156",
    "Análises e Previsões (IA)",
    "Chamados SEDEC", 
    "Infraestrutura e Serviços",
    "Chatbot"
))

# Base Coordinates (Recife)
latitude_base = -8.0476
longitude_base = -34.8770

# Define the icons dictionary once
icones = {
    "Lixo": {"icone": "trash", "cor": "green"},
    "Trânsito": {"icone": "car", "cor": "red"},
    "Metrô": {"icone": "train", "cor": "purple"},
    "Zona Azul": {"icone": "info-sign", "cor": "blue"},
    "Acidente": {"icone": "exclamation-sign", "cor": "orange"},
    # Add more icon types as needed
}

# Function to add custom icons to the map using API data
def adicionar_icones_api(mapa, dados, icones, latitude_base, longitude_base):
    for _, row in dados.iterrows():
        tipo = row.get("tipo", "Desconhecido")  # Get 'tipo' column or default
        lat = row.get("latitude", latitude_base)  # Get latitude or default
        lon = row.get("longitude", longitude_base)  # Get longitude or default
        
        if tipo in icones:
            folium.Marker(
                location=[lat, lon],
                popup=tipo,  # Add more info from data
                icon=folium.Icon(color=icones[tipo]["cor"], 
                                 icon=icones[tipo]["icone"], 
                                 prefix='glyphicon')
            ).add_to(mapa)

# Function to add custom icons to the map using simulated data
def adicionar_icones_simulados(mapa, icones, latitude_base, longitude_base, num_markers=15):
    for i in range(num_markers):
        tipo = random.choice(list(icones.keys()))
        lat_offset = random.uniform(-0.01, 0.01)
        lon_offset = random.uniform(-0.01, 0.01)
        folium.Marker(
            location=[latitude_base + lat_offset, longitude_base + lon_offset],
            popup=f"{tipo} #{i+1}",
            icon=folium.Icon(color=icones[tipo]["cor"], 
                             icon=icones[tipo]["icone"], 
                             prefix='glyphicon')
        ).add_to(mapa)

# Handling different menu options
if aba == "Mapa Interativo":
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
    
    # Choose between API data or simulated data:
    # df_156 = carregar_dados_156()
    # adicionar_icones_api(mapa, df_156, icones, latitude_base, longitude_base) 
    adicionar_icones_simulados(mapa, icones, latitude_base, longitude_base)  # Using simulated data for now
    
    folium_static(mapa)

elif aba == "Ocorrências 156":
    # Placeholder for future functionalities
    pass

elif aba == "Análises e Previsões (IA)":
    st.subheader("📊 Análises e Previsões com IA")
    st.markdown("""
    Essa seção usa modelos de inteligência artificial para gerar insights:
    - **Previsão de volume de chamadas 156:** (Prophet/ARIMA - Em breve)
    - **Identificação de áreas críticas:** (KMeans - Em breve)
    - **Classificação de ocorrências:** (NLP - Em breve)
    - **Detecção de anomalias:** (Em breve)
    """)
    
    # Placeholder for future functionalities:
    # if st.button("📈 Gerar Previsões"):
    #     # ... (Prophet/ARIMA code here) 
    # if st.button("📍 Identificar Áreas Críticas"):
    #     # ... (KMeans code here)

# ... (rest of the code for other sections - Chamados SEDEC, Infraestrutura, Chatbot)
Summary of Changes
