import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
from datetime import datetime
import openai

st.set_page_config(page_title="Transporte Inteligente", layout="wide")
st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Sidebar
modo = st.sidebar.radio("👤 Modo de Visualização", ["Usuário", "Gestor"])
aba = st.sidebar.radio("Escolha uma opção:", ("Mapa Interativo", "Ocorrências 156", "Chamados SEDEC", "Infraestrutura e Serviços", "Chatbot"))

# Base - localização Recife
latitude_base = -8.0476
longitude_base = -34.8770

# Função para criar posições aleatórias
def gerar_posicao_proxima(base_lat, base_lon, variacao=0.01):
    return base_lat + random.uniform(-variacao, variacao), base_lon + random.uniform(-variacao, variacao)

# ===================== ABA: MAPA INTERATIVO =====================
if aba == "Mapa Interativo":
    st.header("🗺️ Mapa Interativo da Mobilidade Urbana")
    m = folium.Map(location=[latitude_base, longitude_base], zoom_start=12)

    camadas = [
        {"nome": "Ônibus", "cor": "blue", "icone": "bus"},
        {"nome": "BRT", "cor": "green", "icone": "road"},
        {"nome": "VLT", "cor": "red", "icone": "train"},
        {"nome": "Bicicletário", "cor": "orange", "icone": "bicycle"},
        {"nome": "Terminal", "cor": "purple", "icone": "flag"},
        {"nome": "Lixo", "cor": "black", "icone": "trash"},
        {"nome": "Escolar", "cor": "cadetblue", "icone": "graduation-cap"},
        {"nome": "Metrô", "cor": "darkpurple", "icone": "subway"},
        {"nome": "Emergência", "cor": "darkred", "icone": "ambulance"},
        {"nome": "Trânsito", "cor": "lightgray", "icone": "car"},
        {"nome": "Estacionamento", "cor": "lightblue", "icone": "parking"},
        {"nome": "Zona Azul", "cor": "beige", "icone": "ticket"},
    ]

    for camada in camadas:
        for _ in range(3):
            lat, lon = gerar_posicao_proxima(latitude_base, longitude_base)
            folium.Marker(
                location=[lat, lon],
                popup=camada["nome"],
                icon=folium.Icon(color=camada["cor"], icon=camada["icone"], prefix="fa")
            ).add_to(m)

    folium_static(m)

# ===================== ABA: OCORRÊNCIAS 156 =====================
elif aba == "Ocorrências 156":
    st.header("📋 Solicitações 156 em Tempo Real")
    try:
        df_156 = pd.read_csv("156_cco_diario.csv")
        st.dataframe(df_156)
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo 156_cco_diario.csv: {e}")

# ===================== ABA: CHAMADOS SEDEC =====================
elif aba == "Chamados SEDEC":
    st.header("🚨 Chamados SEDEC em Tempo Real")
    try:
        df_sedec = pd.read_csv("sedec_chamados_tempo_real.csv")
        st.dataframe(df_sedec)
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo sedec_chamados_tempo_real.csv: {e}")

# ===================== ABA: INFRAESTRUTURA =====================
elif aba == "Infraestrutura e Serviços":
    st.header("🏗️ Infraestrutura e Monitoramento")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📹 Monitoramento CTTU")
        try:
            df_monitoramento = pd.read_csv("monitoramentocttu.csv")
            st.dataframe(df_monitoramento)
        except Exception as e:
            st.error(f"Erro ao carregar monitoramentocttu.csv: {e}")

    with col2:
        st.subheader("📍 Equipamentos de Fiscalização")
        try:
            df_equip = pd.read_csv("equipamentosfiscalizacao.csv")
            st.dataframe(df_equip)
        except Exception as e:
            st.error(f"Erro ao carregar equipamentosfiscalizacao.csv: {e}")

    st.subheader("📊 Tipos de Ocorrências (SEDEC)")
    try:
        df_ocorrencias = pd.read_csv("sedec_tipo_ocorrencias_tempo_real.csv")
        st.dataframe(df_ocorrencias)
    except Exception as e:
        st.error(f"Erro ao carregar sedec_tipo_ocorrencias_tempo_real.csv: {e}")

# ===================== ABA: CHATBOT =====================
elif aba == "Chatbot":
    st.header("🤖 Chatbot Inteligente")
    st.markdown("Converse com nosso assistente sobre mobilidade urbana, serviços públicos e mais.")

    try:
        openai.api_key = st.secrets["openai_api_key"]

        if "mensagens" not in st.session_state:
            st.session_state.mensagens = [{"role": "system", "content": "Você é um assistente especializado em mobilidade urbana e serviços públicos no Recife."}]

        pergunta = st.text_input("Faça sua pergunta:")

        if pergunta:
            st.session_state.mensagens.append({"role": "user", "content": pergunta})
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.mensagens
            )
            resposta_texto = resposta.choices[0].message["content"]
            st.session_state.mensagens.append({"role": "assistant", "content": resposta_texto})
            st.success(resposta_texto)

    except Exception as e:
        st.error(f"Erro ao usar o Chatbot: {e}")

