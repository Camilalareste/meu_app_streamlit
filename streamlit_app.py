# Configuração da Página
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from statsmodels.tsa.arima.model import ARIMA
from sklearn.cluster import KMeans
import numpy as np
import random

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

# Coordenadas Base (Recife)
latitude_base = -8.0476
longitude_base = -34.8770

# Função para carregar dados dos arquivos CSV
def carregar_dados():
    try:
        dados_156 = pd.read_csv("156_cco_diario.csv")
    except pd.errors.ParserError as e:
        st.error(f"Erro ao ler o arquivo CSV '156_cco_diario.csv': {e}")
        return None
    
    coleta = pd.read_csv("coleta.csv")
    equipamentos = pd.read_csv("equipamentosfiscalizacao.csv")
    fluxo_velocidade = pd.read_csv("fluxovelocidadeemquinzeminuto-foto-jan-25.csv")
    monitoramento_cttu = pd.read_csv("monitoramentocttu.csv")
    pontos_coleta = pd.read_csv("pontos_coleta.csv")
    sedec_chamados = pd.read_csv("sedec_chamados_tempo_real.csv")
    sedec_tipo_ocorrencias = pd.read_csv("sedec_tipo_ocorrencias_tempo_real.csv")
    sedec_vistorias = pd.read_csv("sedec_vistorias_tempo_real.csv")

    return {
        "dados_156": dados_156,
        "coleta": coleta,
        "equipamentos": equipamentos,
        "fluxo_velocidade": fluxo_velocidade,
        "monitoramento_cttu": monitoramento_cttu,
        "pontos_coleta": pontos_coleta,
        "sedec_chamados": sedec_chamados,
        "sedec_tipo_ocorrencias": sedec_tipo_ocorrencias,
        "sedec_vistorias": sedec_vistorias,
    }

# Carregar todos os dados
dados = carregar_dados()
if dados is None:
    st.stop()

# Função para adicionar ícones personalizados ao mapa
def adicionar_icones(mapa, dados, tipo_dado, lat_col='latitude', lon_col='longitude', popup_col=None):
    for _, row in dados.iterrows():
        lat = row[lat_col]
        lon = row[lon_col]
        popup_text = row[popup_col] if popup_col else tipo_dado
        folium.Marker(
            location=[lat, lon],
            popup=popup_text
        ).add_to(mapa)

# Função para previsões com ARIMA
def previsao_arima(dados, coluna, passos=10):
    modelo = ARIMA(dados[coluna], order=(5, 1, 0))
    modelo_fit = modelo.fit(disp=0)
    previsoes = modelo_fit.forecast(steps=passos)[0]
    return previsoes

# Função para clustering com KMeans
def clustering_kmeans(dados, n_clusters=5):
    coordenadas = dados[['latitude', 'longitude']].dropna()
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(coordenadas)
    dados['cluster'] = kmeans.labels_
    return dados, kmeans.cluster_centers_

# Exibir os dados carregados
if aba == "Mapa Interativo":
    st.subheader("Mapa Interativo")
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

    # Adicionar dados ao mapa
    adicionar_icones(mapa, dados["pontos_coleta"], "Pontos de Coleta", popup_col='nome')
    adicionar_icones(mapa, dados["equipamentos"], "Equipamentos de Fiscalização")

    folium_static(mapa)

elif aba == "Ocorrências 156":
    st.subheader("Ocorrências 156")
    st.dataframe(dados["dados_156"])

elif aba == "Análises e Previsões (IA)":
    st.subheader("📊 Análises e Previsões com IA")
    st.markdown("""
    Essa seção usa modelos de inteligência artificial para gerar insights:
    - **Previsão de volume de chamadas 156:** Usando ARIMA
    - **Identificação de áreas críticas:** Usando KMeans
    - **Classificação de ocorrências:** (NLP - Em breve)
    - **Detecção de anomalias:** (Em breve)
    """)

    # Exemplo de Previsão ARIMA
    if st.button("📈 Gerar Previsões ARIMA"):
        previsoes = previsao_arima(dados["dados_156"], 'quantidade')
        st.write("Previsões de Chamadas 156 para os próximos dias:", previsoes)

    # Exemplo de Clustering KMeans
    if st.button("📍 Identificar Áreas Críticas com KMeans"):
        dados_clusterizados, centros = clustering_kmeans(dados["dados_156"])
        st.dataframe(dados_clusterizados)

        mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
        for centro in centros:
            folium.Marker(location=centro, popup="Centro do Cluster").add_to(mapa)
        folium_static(mapa)

elif aba == "Chamados SEDEC":
    st.subheader("Chamados SEDEC")
    st.dataframe(dados["sedec_chamados"])

elif aba == "Infraestrutura e Serviços":
    st.subheader("Infraestrutura e Serviços")
    st.dataframe(dados["equipamentos"])

elif aba == "Chatbot":
    st.subheader("Chatbot")
    st.text("Funcionalidade do Chatbot em desenvolvimento")

# Adicionar mais funcionalidades conforme necessário
