# Configuração da Página
import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
import requests
from folium.plugins import MarkerCluster

# Configuração da Página
st.set_page_config(page_title="Plataforma de Mobilidade Urbana", layout="wide")

# Título
st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Barra Lateral: Modo de Visualização e Menu Principal
modo = st.sidebar.radio("👤 Modo de Visualização", ["Usuário", "Gestor"])
aba = st.sidebar.radio("Menu Principal", (
    "Mapa Interativo",
    "Ocorrências 156",
    "Análises e Previsões (IA)",
    "Chamados SEDEC", 
    "Infraestrutura e Serviços",
    "Chatbot"
))

# Adicionar mensagem de depuração para verificar a aba selecionada
st.write(f"Aba selecionada: {aba}")

# Coordenadas Base (Recife)
latitude_base = -8.0476
longitude_base = -34.8770

# Definir o dicionário de ícones uma vez
icones = {
    "Lixo": {"icone": "trash", "cor": "green"},
    "Trânsito": {"icone": "car", "cor": "red"},
    "Metrô": {"icone": "train", "cor": "purple"},
    "Zona Azul": {"icone": "info-sign", "cor": "blue"},
    "Acidente": {"icone": "exclamation-sign", "cor": "orange"},
    # Adicione mais tipos de ícones conforme necessário
}

# Função para adicionar ícones personalizados ao mapa usando dados da API
def adicionar_icones_api(mapa, dados, icones, latitude_base, longitude_base):
    for _, row in dados.iterrows():
        tipo = row.get("tipo", "Desconhecido")  # Obter coluna 'tipo' ou padrão
        lat = row.get("latitude", latitude_base)  # Obter latitude ou padrão
        lon = row.get("longitude", longitude_base)  # Obter longitude ou padrão
        
        if tipo in icones:
            folium.Marker(
                location=[lat, lon],
                popup=tipo,  # Adicionar mais informações dos dados
                icon=folium.Icon(color=icones[tipo]["cor"], 
                                 icon=icones[tipo]["icone"], 
                                 prefix='glyphicon')
            ).add_to(mapa)

# Função para adicionar ícones personalizados ao mapa usando dados simulados
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

# Tratando diferentes opções do menu
if aba == "Mapa Interativo":
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
    
    # Escolha entre dados da API ou dados simulados:
    # df_156 = carregar_dados_156()
    # adicionar_icones_api(mapa, df_156, icones, latitude_base, longitude_base) 
    adicionar_icones_simulados(mapa, icones, latitude_base, longitude_base)  # Usando dados simulados por enquanto
    
    folium_static(mapa)

elif aba == "Ocorrências 156":
    # Placeholder para funcionalidades futuras
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
    
    # Placeholder para funcionalidades futuras:
    # if st.button("📈 Gerar Previsões"):
    #     # ... (código Prophet/ARIMA aqui) 
    # if st.button("📍 Identificar Áreas Críticas"):
    #     # ... (código KMeans aqui)

# ... (restante do código para outras seções - Chamados SEDEC, Infraestrutura, Chatbot)
