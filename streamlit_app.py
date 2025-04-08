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
                icon=folium.Icon(color=icones[tipo]["cor"],
                                 icon=icones[tipo]["icone"],
                                 prefix='glyphicon')
            ).add_to(mapa)

# Function to load data from an API with a given resource ID
@st.cache_data
def carregar_dados_api(resource_id):
    url_api = "http://dados.recife.pe.gov.br/api/3/action/datastore_search"
    params = {
        'resource_id': resource_id,
        'limit': 100
    }
    try:
        response = requests.get(url_api, params=params)
        data = response.json()
        if data and data.get('success') and data.get('result') and data['result'].get('records'):
            records = data['result']['records']
            return pd.DataFrame(records)
        else:
            st.warning(f"⚠️ API request successful for resource ID '{resource_id}', but no data records found.")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao carregar dados da API (resource ID '{resource_id}'): {e}")
        return pd.DataFrame()

# Handling different menu options
if aba == "Mapa Interativo":
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
    adicionar_icones(mapa)  # Using simulated data for now
    folium_static(mapa)
elif aba == "Ocorrências 156":
    st.subheader("📋 Dados de Mobilidade")
    df_mobilidade_1 = carregar_dados_api('5b96a34d-06c9-4103-9717-1fdf0af5aee1')
    df_mobilidade_2 = carregar_dados_api('9afa68cf-7fd9-4735-b157-e23da873fef7')
    
    if not df_mobilidade_1.empty:
        st.success("✅ Dados de mobilidade 1 carregados com sucesso!")
        st.dataframe(df_mobilidade_1)
    else:
        st.warning("⚠️ Nenhum dado de mobilidade 1 encontrado.")
    
    if not df_mobilidade_2.empty:
        st.success("✅ Dados de mobilidade 2 carregados com sucesso!")
        st.dataframe(df_mobilidade_2)
    else:
        st.warning("⚠️ Nenhum dado de mobilidade 2 encontrado.")    
elif aba == "Análises e Previsões (IA)":
    st.subheader("📊 Análises e Previsões com IA")
    st.markdown("""
    Essa seção usa modelos de inteligência artificial para gerar insights:
    - Previsão de volume de chamadas 156 (Prophet/ARIMA - Em breve)
    - Identificação de áreas críticas (KMeans - Em breve)
    - Classificação de ocorrências (NLP - Em breve)
    - Detecção de anomalias (Em breve)
    """)
elif aba == "Chamados SEDEC":
    st.subheader("🆘 Chamados da Defesa Civil (SEDEC)")
    st.info("🔧 Em breve integração com dados de chamados da Defesa Civil")
elif aba == "Infraestrutura e Serviços":
    st.subheader("🏗️ Monitoramento de Infraestrutura Urbana")
    st.info("📡 Módulo em desenvolvimento com dados sobre semáforos, câmeras e sensores")
elif aba == "Chatbot":
    st.subheader("🤖 Chatbot Inteligente para Dúvidas sobre Mobilidade")
    st.info("💬 Em breve integração com modelo conversacional para responder dúvidas do cidadão.")

# ... other imports
import random
import requests
# Add these imports
import plotly.express as px  # For plotting charts

# ... other imports
import random
import requests
# Add these imports
import plotly.express as px  # For plotting charts

elif aba == "Análises e Previsões (IA)":
    st.subheader("📊 Análises e Previsões com IA")
    st.markdown("""
    Essa seção usa modelos de inteligência artificial para gerar insights:
    - Previsão de volume de chamadas 156
    - Identificação de áreas críticas
    - Classificação de ocorrências
    - Detecção de anomalias
    """)

    if st.button("📈 Gerar Previsões"):
        st.success("🔮 Previsões geradas com base em dados históricos (exemplo hipotético)")
        
        # Generate random data for demonstration
        df_previsoes = pd.DataFrame({
            "Dia": range(1, 8),  # Simulate 7 days
            "Chamadas 156": [random.randint(20, 100) for _ in range(7)],
            "Acidentes": [random.randint(5, 20) for _ in range(7)],
        })

        # Create a line chart using Plotly Express
        fig = px.line(df_previsoes, x="Dia", y=["Chamadas 156", "Acidentes"], title="Previsões para os Próximos 7 Dias")
        st.plotly_chart(fig)

    if st.button("💡 Gerar Recomendações Inteligentes"):
        st.info("🚨 Região com maior volume de ocorrências: Boa Vista")
        st.info("🚧 Sugestão: Aumentar fiscalização na Av. Agamenon Magalhães")
         Plataforma de Mobilidade Urbana Inteligente
st.subheader("Análises e Previsões com IA")
Essa seção usa modelos de inteligência artificial para gerar insights:

Previsão de volume de chamadas 156 (Prophet/ARIMA - Em breve)
Identificação de áreas críticas (KMeans - Em breve)
Classificação de ocorrências (NLP - Em breve)
Detecção de anomalias (Em breve)
import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
import requests
from folium.plugins import MarkerCluster
import plotly.express as px  # For plotting charts

# Import for AI features, handling potential errors
try:
    from prophet import Prophet
    from sklearn.cluster import KMeans
except ImportError:
    st.warning("Some AI features might not be available. Install 'prophet' and 'scikit-learn' for full functionality.")
def prever_chamadas_156():
    # Your Prophet/ARIMA implementation will go here
    st.info("Previsão de chamadas 156 em desenvolvimento.")

def identificar_areas_criticas():
    # Your KMeans implementation will go here
    st.info("Identificação de áreas críticas em desenvolvimento.")

def classificar_ocorrencias():
    # Your NLP implementation will go here
    st.info("Classificação de ocorrências em desenvolvimento.")

def detectar_anomalias():
    # Your anomaly detection implementation will go here
    st.info("Detecção de anomalias em desenvolvimento.")
elif aba == "Análises e Previsões (IA)":
    st.subheader("📊 Análises e Previsões com IA")
    st.markdown("""
    Essa seção usa modelos de inteligência artificial para gerar insights:
    - Previsão de volume de chamadas 156
    - Identificação de áreas críticas
    - Classificação de ocorrências
    - Detecção de anomalias
    """)

    if st.button("📈 Gerar Previsões"):
        prever_chamadas_156()  # Call the function

    if st.button("📍 Identificar Áreas Críticas"):
        identificar_areas_criticas()  # Call the function

    # Add buttons for other AI features
    if st.button("📝 Classificar Ocorrências"):
        classificar_ocorrencias()

    if st.button("⚠️ Detectar Anomalias"):
        detectar_anomalias()
        
