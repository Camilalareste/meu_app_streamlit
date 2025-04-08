import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from datetime import datetime
import random

# Configuração inicial da página
st.set_page_config(page_title="Plataforma de Mobilidade Urbana Inteligente", layout="wide", initial_sidebar_state="expanded")
st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Sidebar - Navegação entre abas
aba = st.sidebar.radio("Escolha uma opção:", [
    "Mapa Interativo",
    "Ocorrências 156",
    "Chamados SEDEC",
    "Infraestrutura e Serviços",
    "Chatbot"
])

# Função para gerar dados fictícios

def gerar_dados_ficticios(categoria, n=10):
    base_lat, base_lon = -8.0476, -34.8770
    dados = []
    for _ in range(n):
        dados.append({
            "categoria": categoria,
            "latitude": base_lat + random.uniform(-0.01, 0.01),
            "longitude": base_lon + random.uniform(-0.01, 0.01),
            "descricao": f"Ocorrência de {categoria}",
            "horario": datetime.now().strftime("%H:%M")
        })
    return pd.DataFrame(dados)

# Dados fictícios
categorias = ["Lixo", "Escolar", "Metrô", "Emergência", "Trânsito", "Estacionamento"]
dados_por_categoria = {cat: gerar_dados_ficticios(cat) for cat in categorias}

# Mapa Interativo
if aba == "Mapa Interativo":
    st.header("🗺️ Mapa Interativo com Ocorrências e Infraestrutura")
    mapa = folium.Map(location=[-8.0476, -34.8770], zoom_start=13)

    # Adiciona pinos de cada categoria
    icones = {
        "Lixo": "trash",
        "Escolar": "graduation-cap",
        "Metrô": "subway",
        "Emergência": "ambulance",
        "Trânsito": "car",
        "Estacionamento": "parking"
    }

    for cat, df in dados_por_categoria.items():
        for _, row in df.iterrows():
            folium.Marker(
                [row["latitude"], row["longitude"]],
                popup=f"{cat}: {row['descricao']}\nHorário: {row['horario']}",
                icon=folium.Icon(color="blue", icon=icones[cat], prefix='fa')
            ).add_to(mapa)

    folium_static(mapa)

# Ocorrências 156
elif aba == "Ocorrências 156":
    st.header("📋 Solicitações 156 em Tempo Real")
    try:
        df_156 = pd.read_csv("156_cco_diario.csv")
        st.dataframe(df_156)
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo 156_cco_diario.csv: {e}")

# Chamados SEDEC
elif aba == "Chamados SEDEC":
    st.header("🚨 Chamados SEDEC em Tempo Real")
    try:
        df_sedec = pd.read_csv("sedec_chamados_tempo_real.csv")
        st.dataframe(df_sedec)
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo sedec_chamados_tempo_real.csv: {e}")

# Infraestrutura e Serviços
elif aba == "Infraestrutura e Serviços":
    st.header("🔧 Visão Geral da Infraestrutura e Serviços")
    aba_servico = st.selectbox("Escolha a categoria:", categorias)
    st.subheader(f"Ocorrências de {aba_servico}")
    st.dataframe(dados_por_categoria[aba_servico])

# Chatbot (simples)
elif aba == "Chatbot":
    st.header("🤖 Chatbot de Atendimento")
    pergunta = st.text_input("Digite sua pergunta sobre mobilidade urbana:")
    if pergunta:
        st.write(f"🔎 Ainda estamos treinando nosso assistente. Sua pergunta foi: '{pergunta}'")
