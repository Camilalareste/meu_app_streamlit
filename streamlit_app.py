 
import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import folium_static
from datetime import datetime
# import openai  # Descomente se for usar o ChatGPT

# Configuração da página
st.set_page_config(page_title="Transporte Inteligente", layout="wide")

# Título principal
st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Sidebar: modo de visualização e menu principal
modo = st.sidebar.radio("👤 Modo de Visualização", ["Usuário", "Gestor"])
aba = st.sidebar.radio("📂 Menu Principal", (
    "Mapa Interativo",
    "Ocorrências 156",
    "Chamados SEDEC",
    "Infraestrutura e Serviços",
    "Chatbot"
))

# Função para carregar dados 156 via API CKAN
@st.cache_data
def carregar_dados_156():
    resource_id = "9afa68cf-7fd9-4735-b157-e23da873fef7"  # ID do recurso CSV
    url = f"http://dados.recife.pe.gov.br/api/3/action/datastore_search?resource_id={resource_id}&limit=1000"
    try:
        response = requests.get(url)
        data = response.json()
        records = data['result']['records']
        df = pd.DataFrame.from_records(records)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados da API 156: {e}")
        return pd.DataFrame()

# 📍 Aba: Ocorrências 156
if aba == "Ocorrências 156":
    st.subheader("📋 Solicitações 156 em Tempo Real")

    df_156 = carregar_dados_156()

    if not df_156.empty:
        st.success("✅ Dados 156 carregados com sucesso da API!")
        st.dataframe(df_156.head(20), use_container_width=True)
    else:
        st.warning("⚠️ Não foi possível carregar os dados do 156.")

# 🗺️ Aba: Mapa Interativo
elif aba == "Mapa Interativo":
    st.subheader("🗺️ Mapa Interativo de Mobilidade")
    
    m = folium.Map(location=[-8.0476, -34.8770], zoom_start=12)
    folium.Marker(
        [-8.0476, -34.8770],
        tooltip="Prefeitura do Recife",
        icon=folium.Icon(color='blue')
    ).add_to(m)

    folium_static(m)

# 📊 Aba: Chamados SEDEC
elif aba == "Chamados SEDEC":
    st.subheader("📊 Chamados SEDEC")
    st.info("🚧 Em desenvolvimento: aqui serão exibidos os chamados em tempo real da Defesa Civil (SEDEC).")

# 🏗️ Aba: Infraestrutura e Serviços
elif aba == "Infraestrutura e Serviços":
    st.subheader("🏗️ Infraestrutura e Monitoramento")
    st.info("🚧 Em breve: visualização de câmeras, equipamentos de fiscalização e semáforos inteligentes.")

# 🤖 Aba: Chatbot
elif aba == "Chatbot":
    st.subheader("🤖 Assistente Virtual de Mobilidade")
    st.info("🚧 Em breve: Chatbot com inteligência artificial para atendimento ao cidadão.")
    # openai.api_key = "sua-chave-aqui"
    # user_question = st.text_input("Pergunte algo sobre mobilidade urbana:")
    # if st.button("Enviar") and user_question:
    #     response = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         messages=[{"role": "user", "content": user_question}]
    #     )
    #     st.write(response.choices[0].message["content"])
