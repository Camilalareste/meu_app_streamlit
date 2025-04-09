import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
import requests
from folium.plugins import MarkerCluster
import googlemaps
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Plataforma de Mobilidade Urbana", layout="wide")

# **For AI & Machine Learning (Future implementation)**
from sklearn.cluster import KMeans
from prophet import Prophet

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

# Function to add custom icons to the map (enhanced)
def adicionar_icones(mapa, dados=None):  
    # Allows using data from API or simulated data
    icones = {
        "Lixo": {"icone": "trash", "cor": "green"},
        "Trânsito": {"icone": "car", "cor": "red"},
        "Metrô": {"icone": "train", "cor": "purple"},
        "Zona Azul": {"icone": "info-sign", "cor": "blue"},
        "Acidente": {"icone": "exclamation-sign", "cor": "orange"},
        # Add more icon types as needed
    }

    if dados is not None:
        # Use data from API if provided
        for _, row in dados.iterrows():
            tipo = row.get("tipo", "Desconhecido")  # Get 'tipo' column or default
            lat = row.get("latitude", latitude_base)  # Get latitude or default
            lon = row.get("longitude", longitude_base)  # Get longitude or default
            
            if tipo in icones:
                folium.Marker(
                    location=[lat, lon],
                    popup=tipo, # Add more info from data
                    icon=folium.Icon(color=icones[tipo]["cor"], 
                                     icon=icones[tipo]["icone"], 
                                     prefix='glyphicon')
                ).add_to(mapa)
    else:
        # Use simulated data if no API data is provided
        for i in range(15):
            tipo = random.choice(list(icones.keys()))
            lat_offset = random.uniform(-0.01, 0.01)
            lon_offset = random.uniform(-0.01, 0.01)
            folium.Marker(
                location=[latitude_base + lat_offset, longitude_base + lonoffset],
                popup=f"{tipo} #{i+1}",
                icon=folium.Icon(color=icones[tipo]["cor"], 
                                 icon=icones[tipo]["icone"], 
                                 prefix='glyphicon')
            ).add_to(mapa)

# Handling different menu options
if aba == "Mapa Interativo":
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
    adicionar_icones(mapa)  # Using simulated data for now
    folium_static(mapa)

elif aba == "Ocorrências 156":
    st.subheader("Ocorrências 156")
    st.markdown("Funcionalidade em desenvolvimento.")

elif aba == "Análises e Previsões (IA)":
    st.subheader("📊 Análises e Previsões com IA")
    st.markdown("""
    Essa seção usa modelos de inteligência artificial para gerar insights:
    - **Previsão de volume de chamadas 156:** Usando Prophet
    - **Identificação de áreas críticas:** Usando KMeans
    - **Classificação de ocorrências:** (NLP - Em breve)
    - **Detecção de anomalias:** (Em breve)
    """)
    st.markdown("Funcionalidade em desenvolvimento.")

elif aba == "Chamados SEDEC":
    st.subheader("Chamados SEDEC")
    st.markdown("Funcionalidade em desenvolvimento.")

elif aba == "Infraestrutura e Serviços":
    st.subheader("Infraestrutura e Serviços")
    st.markdown("Funcionalidade em desenvolvimento.")

elif aba == "Chatbot":
    st.subheader("Chatbot")
    user_input = st.text_input("Pergunte ao Chatbot:")
    if st.button("Enviar"):
        st.write("Funcionalidade em desenvolvimento.")
