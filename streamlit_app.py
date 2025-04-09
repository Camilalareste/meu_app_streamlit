import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
import requests
from folium.plugins import MarkerCluster
import plotly.express as px  # Import for plotting

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

# Function to add custom icons to the map
def adicionar_icones(mapa, dados=None):
    icones = {
        "Lixo": {"icone": "trash", "cor": "green"},
        "Trânsito": {"icone": "car", "cor": "red"},
        "Metrô": {"icone": "train", "cor": "purple"},
        "Zona Azul": {"icone": "info-sign", "cor": "blue"},
        "Acidente": {"icone": "exclamation-sign", "cor": "orange"},
    }

    if dados is not None:
        for _, row in dados.iterrows():
            tipo = row.get("tipo", "Desconhecido")
            lat = row.get("latitude", latitude_base)
            lon = row.get("longitude", longitude_base)
            if tipo in icones:
                folium.Marker(
                    location=[lat, lon],
                    popup=tipo,
                    icon=folium.Icon(color=icones[tipo]["cor"],
                                     icon=icones[tipo]["icone"],
                                     prefix='glyphicon')
                ).add_to(mapa)
    else:
        for i in range(15):
            tipo = random.choice(list(icones.keys()))
            lat_offset = random.uniform(-0.01, 0.01)
            lon_offset = random.uniform(-0.01, 0.01)
            folium.Marker(
                location=[latitude_base + lat_offset, longitude_base + lon_offset], 
                popup=f"{tipo} #{i+1}",
                icon=folium.Icon(color=icones[tipo]["cor"], icon=icones[tipo]["icone"], prefix='glyphicon')
            ).add_to(mapa)

# Function to load data from an API with a given resource ID
@st.cache_data
def carregar_dados_api(resource_id):
    # ... (same as before)

# Handling different menu options
if aba == "Mapa Interativo":
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
    adicionar_icones(mapa)  # Using simulated data for now
    folium_static(mapa)
elif aba == "Ocorrências 156":
    # ... (same as before)
elif aba == "Análises e Previsões (IA)":
    # ... (same as before - AI section)
elif aba == "Chamados SEDEC":
    # ... (same as before)
elif aba == "Infraestrutura e Serviços":
    # ... (same as before)
elif aba == "Chatbot":
    # ... (same as before)
