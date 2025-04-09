import streamlit as st
import requests

# Configuração da Página
st.set_page_config(page_title="Plataforma de Mobilidade Urbana", layout="wide")

# Título
st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Barra Lateral: Modo de Visualização e Menu Principal
modo = st.sidebar.radio("👤 Modo de Visualização", ["Usuário", "Gestor"])
aba = st.sidebar.radio("Menu Principal", (
    "Consulta de Dados",
    "Consulta via SQL",
))

# Função para consultar dados via API
def consultar_dados(resource_id, query=None, limit=5):
    base_url = 'http://dados.recife.pe.gov.br/pt_BR/api/3/action/datastore_search'
    params = {
        'resource_id': resource_id,
        'limit': limit,
    }
    if query:
        params['q'] = query

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Erro ao consultar dados: {response.status_code}")
        return None

# Função para consultar dados via SQL
def consultar_dados_sql(resource_id, sql_query):
    base_url = 'http://dados.recife.pe.gov.br/pt_BR/api/3/action/datastore_search_sql'
    params = {
        'sql': f'SELECT * from "{resource_id}" WHERE {sql_query}'
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Erro ao consultar dados via SQL: {response.status_code}")
        return None

# Exibir os dados carregados
if aba == "Consulta de Dados":
    st.subheader("Consulta de Dados")
    resource_id = st.text_input("Resource ID", "9afa68cf-7fd9-4735-b157-e23da873fef7")
    query = st.text_input("Consulta (opcional)", "")
    limit = st.number_input("Limite de resultados", value=5, min_value=1)

    if st.button("Consultar"):
        dados = consultar_dados(resource_id, query, limit)
        if dados:
            st.write("Resultados encontrados:", dados['result']['total'])
            st.json(dados)

elif aba == "Consulta via SQL":
    st.subheader("Consulta via SQL")
    resource_id = st.text_input("Resource ID", "9afa68cf-7fd9-4735-b157-e23da873fef7")
    sql_query = st.text_area("SQL Query", "title LIKE 'jones'")

    if st.button("Consultar via SQL"):
        dados = consultar_dados_sql(resource_id, sql_query)
        if dados:
            st.write("Resultados encontrados:", dados['result']['total'])
            st.json(dados)
