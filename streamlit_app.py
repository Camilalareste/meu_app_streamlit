mport streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
from datetime import datetime
import openai

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

# Localização base (Recife)
latitude_base = -8.0476
longitude_base = -34.8770

# Mapa Interativo
if aba == "Mapa Interativo":
    st.header("🗺️ Mapa Interativo de Eventos")
    mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

    # Dados fictícios para serviços urbanos
    icones_servicos = {
        "Coleta de Lixo": "trash",
        "Acidente": "car-crash",
        "Ônibus Escolar": "school",
        "Metrô": "train",
        "Emergência": "plus",
        "Trânsito": "traffic-light",
        "Estacionamento": "parking",
        "Zona Azul": "money-bill"
    }

    for servico, icone in icones_servicos.items():
        for _ in range(5):
            lat = latitude_base + random.uniform(-0.02, 0.02)
            lon = longitude_base + random.uniform(-0.02, 0.02)
            folium.Marker(
                location=[lat, lon],
                icon=folium.Icon(icon=icone, prefix='fa', color=random.choice(['red', 'green', 'blue', 'orange'])),
                popup=f"{servico}"
            ).add_to(mapa)

    folium_static(mapa)

# Ocorrências 156
elif aba == "Ocorrências 156":
    st.header("📋 Solicitações 156 em Tempo Real")
    try:
        df_156 = pd.read_csv("156_cco_diario.csv.csv")
        st.dataframe(df_156.head())
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo 156_cco_diario.csv: {e}")

# Chamados SEDEC
elif aba == "Chamados SEDEC":
    st.header("🚨 Chamados SEDEC em Tempo Real")
    try:
        df_sedec = pd.read_csv("sedec_chamados_tempo_real.csv.csv")
        st.dataframe(df_sedec.head())
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo sedec_chamados_tempo_real.csv: {e}")

# Infraestrutura e Serviços
elif aba == "Infraestrutura e Serviços":
    st.header("🏗️ Infraestrutura e Monitoramento")

    st.subheader("📹 Monitoramento CTTU")
    try:
        df_monit = pd.read_csv("monitoramentocttu.csv.csv")
        st.dataframe(df_monit.head())
    except Exception as e:
        st.error(f"Erro ao carregar monitoramentocttu.csv: {e}")

    st.subheader("📍 Equipamentos de Fiscalização")
    try:
        df_fisc = pd.read_csv("equipamentosfiscalizacao.csv.csv")
        st.dataframe(df_fisc.head())
    except Exception as e:
        st.error(f"Erro ao carregar equipamentosfiscalizacao.csv: {e}")

    st.subheader("📊 Tipos de Ocorrências (SEDEC)")
    try:
        df_tipos = pd.read_csv("sedec_tipo_ocorrencias_tempo_real.csv.csv")
        st.dataframe(df_tipos.head())
    except Exception as e:
        st.error(f"Erro ao carregar sedec_tipo_ocorrencias_tempo_real.csv: {e}")

# Chatbot
elif aba == "Chatbot":
    st.header("🤖 Assistente Virtual de Mobilidade")
    openai.api_key = st.secrets["openai_api_key"] if "openai_api_key" in st.secrets else ""

    pergunta = st.text_input("Digite sua pergunta:")
    if pergunta:
        with st.spinner("Pensando..."):
            try:
                resposta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": pergunta}]
                )
                st.success(resposta.choices[0].message["content"])
            except Exception as e:
                st.error(f"Erro no chatbot: {e}")
