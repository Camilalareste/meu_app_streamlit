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

# Google Maps API Key
gmaps_api_key = "AIzaSyCkXStpIBQg2hV5hst-oEI1J2cw-iwlokc"
gmaps = googlemaps.Client(key=gmaps_api_key)

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

# Function to get transit directions from Google Maps API
def obter_direcoes_transito(origem, destino):
    now = datetime.now()
    directions_result = gmaps.directions(origem,
                                         destino,
                                         mode="transit",
                                         departure_time=now)
    return directions_result

# Placeholder for Chatbot functionality
def chatbot_responder(input_text):
    # Simulated response logic
    if "melhor rota" in input_text:
        return ("Para ir de Camaragibe para o Cabo, a melhor rota é pegar o metrô para o Recife e depois um ônibus para o Cabo. "
                "O custo total é aproximadamente R$ 7,50. As paradas de ônibus e trem estão sendo monitoradas em tempo real.")
    elif "leitura da energia" in input_text:
        return "A leitura da sua energia será feita no próximo dia 20. Por favor, certifique-se de que o medidor esteja acessível."
    elif "carro do lixo" in input_text:
        return "O carro do lixo passa na sua casa toda terça-feira e sexta-feira às 8h da manhã."
    elif "ocorrência" in input_text:
        return "No momento, há uma ocorrência de via alagada na Av. Recife. Evite essa rota e busque alternativas."
    elif "trânsito" in input_text:
        direcoes = obter_direcoes_transito("Camaragibe", "Cabo de Santo Agostinho")
        return f"Trânsito atualizado: {direcoes}"
    else:
        return "Pergunta não reconhecida. Por favor, pergunte sobre rotas, tipos de transporte, preços, serviços públicos ou ocorrências."

# Function to predict using Prophet
def previsao_prophet(dados, coluna):
    modelo = Prophet()
    df = dados[['date', coluna]].rename(columns={'date': 'ds', coluna: 'y'})
    modelo.fit(df)
    futuro = modelo.make_future_dataframe(periods=30)
    previsao = modelo.predict(futuro)
    return previsao

# Function to perform KMeans clustering
def clustering_kmeans(dados, n_clusters=5):
    coordenadas = dados[['latitude', 'longitude']].dropna()
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(coordenadas)
    dados['cluster'] = kmeans.labels_
    return dados, kmeans.cluster_centers_

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
    - **Previsão de volume de chamadas 156:** Usando Prophet
    - **Identificação de áreas críticas:** Usando KMeans
    - **Classificação de ocorrências:** (NLP - Em breve)
    - **Detecção de anomalias:** (Em breve)
    """)
    
    # Exemplo de Previsão Prophet
    if st.button("📈 Gerar Previsões Prophet"):
        previsoes = previsao_prophet(df_156, 'quantidade')
        st.write(previsoes[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

    # Exemplo de Clustering KMeans
    if st.button("📍 Identificar Áreas Críticas com KMeans"):
        df_clusterizado, centros = clustering_kmeans(df_156)
        st.dataframe(df_clusterizado)
        
        mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
        for centro in centros:
            folium.Marker(location=centro, popup="Centro do Cluster").add_to(mapa)
        folium_static(mapa)

elif aba == "Chamados SEDEC":
    st.subheader("Chamados SEDEC")
    # Load and display SEDEC data (similar to carregar_dados_156)
    st.markdown("Funcionalidade em desenvolvimento.")

elif aba == "Infraestrutura e Serviços":
    st.subheader("Infraestrutura e Serviços")
    # Load and display infrastructure data
    st.markdown("Funcionalidade em desenvolvimento.")

elif aba == "Chatbot":
    st.subheader("Chatbot")
    user_input = st.text_input("Pergunte ao Chatbot:")
    if st.button("Enviar"):
        resposta = chatbot_responder(user_input)
        st.write(resposta)

# Add more functionalities as needed
