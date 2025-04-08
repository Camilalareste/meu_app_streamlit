import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
import requests
from folium.plugins import MarkerCluster

# ... (other imports and page setup)

# Function to load data from an API with a given resource ID
@st.cache_data  # Cache data to improve performance
def carregar_dados_api(resource_id):
    url_api = "http://dados.recife.pe.gov.br/api/3/action/datastore_search"
    params = {
        'resource_id': resource_id,
        'limit': 100  # Adjust the limit as needed
    }
    try:
        response = requests.get(url_api, params=params)
        data = response.json()
        if data and data.get('success') and data.get('result') and data['result'].get('records'):
            records = data['result']['records']
            return pd.DataFrame(records)
        else:
            st.warning(f"⚠️ API request successful for resource ID '{resource_id}', but no data records found.")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao carregar dados da API (resource ID '{resource_id}'): {e}")
        return pd.DataFrame()

# ... (other functions like adicionar_icones)

# In the main part of your script, where you handle menu options:
elif aba == "Ocorrências 156": 
    st.subheader("📋 Dados de Mobilidade")

    # Fetch data for each resource ID
    df_mobilidade_1 = carregar_dados_api('5b96a34d-06c9-4103-9717-1fdf0af5aee1')
    df_mobilidade_2 = carregar_dados_api('9afa68cf-7fd9-4735-b157-e23da873fef7')
   
    # Display the DataFrames (if not empty)
    if not df_mobilidade_1.empty:
        st.success("✅ Dados de mobilidade 1 carregados com sucesso!")
        st.dataframe(df_mobilidade_1)
    else:
        st.warning("⚠️ Nenhum dado de mobilidade 1 encontrado.")

    if not df_mobilidade_2.empty:
        st.success("✅ Dados de mobilidade 2 carregados com sucesso!")
        st.dataframe(df_mobilidade_2)
    else:
        st.warning("⚠️ Nenhum dado de mobilidade 2 encontrado.")

# ... (rest of the code)

File "/mount/src/meu_app_streamlit/streamlit_app.py", line 35
  elif aba == "Ocorrências 156":
  ^
SyntaxError: invalid syntax
