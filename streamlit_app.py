import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from datetime import datetime
import openai
import random

st.set_page_config(page_title="Transporte Inteligente", layout="wide")

st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")
st.markdown("Aplicativo para visualização de dados de mobilidade urbana e serviços públicos em tempo real no Recife.")

# Sidebar
modo = st.sidebar.radio("👤 Modo de Visualização", ["Usuário", "Gestor"])
st.sidebar.markdown("Veja informações úteis de transporte ao seu redor.")

# Abas
aba = st.sidebar.radio("Navegação", ("Mapa Interativo", "Dados 156", "Chamados SEDEC", "Chatbot"))

# Localização base Recife
latitude_base = -8.0476
longitude_base = -34.8770

# Função para criar posições aleatórias perto da base
def gerar_localizacoes(qtd=10):
    return [[
        latitude_base + random.uniform(-0.01, 0.01),
        longitude_base + random.uniform(-0.01, 0.01)
    ] for _ in range(qtd)]

# Mapa Interativo
if aba == "Mapa Interativo":
    st.subheader("🗺️ Mapa Interativo de Ocorrências e Serviços")
    m = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
    for loc in gerar_localizacoes(15):
        folium.Marker(location=loc, icon=folium.Icon(color="red"), popup="Ocorrência").add_to(m)
    folium_static(m)

# Dados 156
elif aba == "Dados 156":
    st.subheader("📋 Solicitações 156 em Tempo Real")
    try:
        df_156 = pd.read_csv("156_cco_diario.csv")
        st.dataframe(df_156)
    except:
        st.error("Erro ao carregar o arquivo 156_cco_diario.csv")

# Chamados SEDEC
elif aba == "Chamados SEDEC":
    st.subheader("🚨 Chamados SEDEC em Tempo Real")
    try:
        df_sedec = pd.read_csv("sedec_chamados_tempo_real.csv")
        st.dataframe(df_sedec)
    except:
        st.error("Erro ao carregar o arquivo sedec_chamados_tempo_real.csv")

# Chatbot
elif aba == "Chatbot":
    st.subheader("🤖 Assistente Inteligente")
    user_input = st.text_input("Digite sua pergunta:")
    if user_input:
        with st.spinner("Pensando..."):
            try:
                resposta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_input}]
                )
                st.success(resposta.choices[0].message['content'])
            except Exception as e:
                st.error(f"Erro ao processar resposta: {e}")


