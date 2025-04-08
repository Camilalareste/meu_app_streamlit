import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from datetime import datetime
import random
import openai

st.set_page_config(page_title="Transporte Inteligente", layout="wide")

st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Sidebar com modo de visualização
modo = st.sidebar.radio("👤 Modo de Visualização", ["Usuário", "Gestor"])
aba = st.sidebar.radio("Escolha uma opção:", ("Mapa Interativo", "Ocorrências 156", "Chamados SEDEC", "Infraestrutura e Serviços", "Chatbot"))

# Base do mapa - Recife
latitude_base = -8.0476
longitude_base = -34.8770

# Função de dados simulados para infraestruturas
infraestruturas = [
    {"tipo": "Coleta de Lixo", "icone": "trash", "cor": "green"},
    {"tipo": "Ônibus Escolar", "icone": "graduation-cap", "cor": "orange"},
    {"tipo": "Metrô", "icone": "subway", "cor": "blue"},
    {"tipo": "Emergência", "icone": "plus", "cor": "red"},
    {"tipo": "Trânsito", "icone": "car", "cor": "darkred"},
    {"tipo": "Estacionamento Zona Azul", "icone": "parking", "cor": "cadetblue"}
]

def gerar_pontos(tipo):
    return [
        {
            "lat": latitude_base + random.uniform(-0.01, 0.01),
            "lon": longitude_base + random.uniform(-0.01, 0.01),
            "descricao": f"{tipo} ativo em {datetime.now().strftime('%H:%M:%S')}"
        }
        for _ in range(random.randint(2, 5))
    ]

if aba == "Mapa Interativo":
    st.header("🗺️ Mapa Interativo de Serviços e Infraestrutura")
    m = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

    for infra in infraestruturas:
        pontos = gerar_pontos(infra['tipo'])
        for ponto in pontos:
            folium.Marker(
                location=[ponto['lat'], ponto['lon']],
                popup=ponto['descricao'],
                icon=folium.Icon(color=infra['cor'], icon=infra['icone'], prefix='fa')
            ).add_to(m)

    folium_static(m, width=1100)

if aba == "Ocorrências 156":
    st.header("📋 Solicitações 156 em Tempo Real")
    try:
        df_156 = pd.read_csv("156_cco_diario.csv")
        st.dataframe(df_156)
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo 156_cco_diario.csv: {e}")

if aba == "Chamados SEDEC":
    st.header("📟 Chamados SEDEC em Tempo Real")
    try:
        df_sedec = pd.read_csv("sedec_chamados_tempo_real.csv")
        st.dataframe(df_sedec)
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo sedec_chamados_tempo_real.csv: {e}")

if aba == "Infraestrutura e Serviços":
    st.header("🏗️ Infraestrutura e Serviços Urbanos")
    for infra in infraestruturas:
        st.subheader(f"🔹 {infra['tipo']}")
        dados = gerar_pontos(infra['tipo'])
        st.table(pd.DataFrame(dados))

if aba == "Chatbot":
    st.header("🤖 Assistente Virtual")
    pergunta = st.text_input("Digite sua pergunta:")
    if pergunta:
        st.info("Chatbot em construção. Em breve você poderá interagir com um assistente inteligente!")
