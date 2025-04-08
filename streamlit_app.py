import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import requests
from datetime import datetime
import openai

# Configuração da página
st.set_page_config(page_title="Transporte Inteligente", layout="wide")
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

# Função para carregar dados da API CKAN (ex: dados 156)
def carregar_dados_ckan(resource_id):
    url = "http://dados.recife.pe.gov.br/api/3/action/datastore_search"
    try:
        response = requests.get(url, params={"resource_id": resource_id, "limit": 500})
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data["result"]["records"])
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados da API: {e}")
        return pd.DataFrame()

# Mapa Interativo
if aba == "Mapa Interativo":
    st.subheader("🗺️ Visualização Interativa")
    m = folium.Map(location=[-8.0476, -34.8770], zoom_start=12)
    folium.Marker(location=[-8.0476, -34.8770], popup="Prefeitura do Recife").add_to(m)
    folium_static(m, width=1000, height=500)

# Ocorrências 156
elif aba == "Ocorrências 156":
    st.subheader("📋 Solicitações 156 em Tempo Real")
    resource_id_156 = "9afa68cf-7fd9-4735-b157-e23da873fef7"  # ID do recurso no CKAN
    df_156 = carregar_dados_ckan(resource_id_156)
    if not df_156.empty:
        st.success("✅ Dados 156 carregados com sucesso da API!")
        st.dataframe(df_156)
    else:
        st.warning("⚠️ Dados 156 não disponíveis no momento.")

# Chamados SEDEC
elif aba == "Chamados SEDEC":
    st.subheader("📞 Chamados da Defesa Civil (SEDEC)")
    st.info("🔧 Em breve: integração com API da SEDEC ou upload manual.")
    # Exemplo de como seria:
    # df_sedec = carregar_dados_ckan("ID_DO_RECURSO_SEDEC")
    # st.dataframe(df_sedec)

# Infraestrutura e Serviços
elif aba == "Infraestrutura e Serviços":
    st.subheader("🏗️ Infraestrutura e Monitoramento")
    st.markdown("### 📹 Monitoramento CTTU")
    st.info("🔧 Em breve: integração com dados de câmeras e fiscalização da CTTU.")

    st.markdown("### 📍 Equipamentos de Fiscalização")
    st.info("🔧 Em breve: mapas e dashboards com localizações de radares, sensores, etc.")

# Chatbot
elif aba == "Chatbot":
    st.subheader("🤖 Chatbot de Mobilidade Urbana")

    openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else None
    pergunta = st.text_input("Pergunte algo sobre mobilidade urbana no Recife:")

    if st.button("Enviar") and pergunta:
        if openai.api_key:
            try:
                resposta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": pergunta}]
                )
                st.success(resposta.choices[0].message["content"])
            except Exception as e:
                st.error(f"Erro ao consultar a OpenAI: {e}")
        else:
            st.warning("🔐 Configure sua chave da OpenAI em `st.secrets`.")

