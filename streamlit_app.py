import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
import requests
from folium.plugins import MarkerCluster

# **For AI & Machine Learning (Future implementation)**
# from sklearn.cluster import KMeans
# from prophet import Prophet

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
                location=[latitude_base + lat_offset, longitude_base + lon_offset],
                popup=f"{tipo} #{i+1}",
                icon=folium.Icon(color=icones[tipo]["cor"], 
                                 icon=icones[tipo]["icone"], 
                                 prefix='glyphicon')
            ).add_to(mapa)

# Function to load data from CKAN API
@st.cache_data  
def carregar_dados_156():
    resource_id = "9afa68cf-7fd9-4735-b157-e23da873fef7"
    url = f"http://dados.recife.pe.gov.br/pt_BR/api/3/action/datastore_search?resource_id={resource_id}&limit=1000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        records = data['result']['records']
        return pd.DataFrame(records)
    else:
        st.error("Erro ao carregar dados da API.")
        return pd.DataFrame()

# Handling different menu options
if aba == "Mapa Interativo":
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
    
    # Choose between API data or simulated data:
    df_156 = carregar_dados_156()
    adicionar_icones(mapa, dados=df_156) 
    # adicionar_icones(mapa)  # Using simulated data for now
    
    folium_static(mapa)

elif aba == "Ocorrências 156":
    st.subheader("Ocorrências 156")
    df_156 = carregar_dados_156()
    st.dataframe(df_156)

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

elif aba == "Chamados SEDEC":
    st.subheader("Chamados SEDEC")
    # Load and display SEDEC data (similar to carregar_dados_156)
    # ...

elif aba == "Infraestrutura e Serviços":
    st.subheader("Infraestrutura e Serviços")
    # Load and display infrastructure data
    # ...

elif aba == "Chatbot":
    st.subheader("Chatbot")
    st.text("Funcionalidade do Chatbot em desenvolvimento")

# Add more functionalities as needed

import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
import requests
from folium.plugins import MarkerCluster

# **For AI & Machine Learning (Future implementation)**
# from sklearn.cluster import KMeans
# from prophet import Prophet

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
                location=[latitude_base + lat_offset, longitude_base + lon_offset],
                popup=f"{tipo} #{i+1}",
                icon=folium.Icon(color=icones[tipo]["cor"], 
                                 icon=icones[tipo]["icone"], 
                                 prefix='glyphicon')
            ).add_to(mapa)

# Function to load data from CKAN API
@st.cache_data  
def carregar_dados_156():
    resource_id = "9afa68cf-7fd9-4735-b157-e23da873fef7"
    url = f"http://dados.recife.pe.gov.br/pt_BR/api/3/action/datastore_search?resource_id={resource_id}&limit=1000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        records = data['result']['records']
        return pd.DataFrame(records)
    else:
        st.error("Erro ao carregar dados da API.")
        return pd.DataFrame()

# Handling different menu options
if aba == "Mapa Interativo":
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
    
    # Choose between API data or simulated data:
    df_156 = carregar_dados_156()
    adicionar_icones(mapa, dados=df_156) 
    # adicionar_icones(mapa)  # Using simulated data for now
    
    folium_static(mapa)

elif aba == "Ocorrências 156":
    st.subheader("Ocorrências 156")
    df_156 = carregar_dados_156()
    st.dataframe(df_156)

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

elif aba == "Chamados SEDEC":
    st.subheader("Chamados SEDEC")
    # Load and display SEDEC data (similar to carregar_dados_156)
    # ...

elif aba == "Infraestrutura e Serviços":
    st.subheader("Infraestrutura e Serviços")
    # Load and display infrastructure data
    # ...

elif aba == "Chatbot":
    st.subheader("Chatbot")
    st.text("Funcionalidade do Chatbot em desenvolvimento")

# Add more functionalities as needed
