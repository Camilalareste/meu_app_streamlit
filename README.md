# meu_app_streamlit
App com conteúdo de documentos do Google Docs  
import streamlit as st
import folium
from streamlit_folium import folium_static
import random

st.set_page_config(page_title="Transporte Inteligente", layout="wide")
st.title("🚍 Mapa Inteligente de Transporte Público")

# Localização base (ex: Recife)
latitude_base = -8.0476
longitude_base = -34.8770

# Criar mapa com folium
m = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

# Dados simulados de ônibus
onibus = [
    {"linha": "101", "lat": -8.047, "lon": -34.88},
    {"linha": "102", "lat": -8.05, "lon": -34.875},
    {"linha": "103", "lat": -8.045, "lon": -34.87},
]

# Dados simulados de acidentes
acidentes = [
    {"tipo": "Acidente leve", "lat": -8.049, "lon": -34.872},
    {"tipo": "Interdição", "lat": -8.043, "lon": -34.878},
]

# Marcadores de ônibus
for bus in onibus:
    folium.Marker(
        location=[bus["lat"], bus["lon"]],
        popup=f"Ônibus linha {bus['linha']}",
        icon=folium.Icon(color='blue', icon='bus', prefix='fa')
    ).add_to(m)

# Marcadores de acidentes
for ac in acidentes:
    folium.Marker(
        location=[ac["lat"], ac["lon"]],
        popup=f"{ac['tipo']}",
        icon=folium.Icon(color='red', icon='exclamation-triangle', prefix='fa')
    ).add_to(m)

# Mostrar mapa
folium_static(m)

# Informações adicionais
st.subheader("ℹ️ Situação Atual")
st.markdown("- 🚦 Trânsito moderado na Av. Recife")
st.markdown("- 🛑 Acidente leve registrado na Av. Boa Viagem")
st.markdown("- 🚍 3 ônibus próximos da sua localização")

# Simulação de alternativas
st.subheader("🧭 Sugestões Inteligentes")
st.markdown("- ✅ Use o metrô linha Sul como alternativa")
st.markdown("- ✅ Evite a Av. Agamenon Magalhães por 20 minutos")
st.markdown("- ✅ Estacione no Shopping Recife (vaga disponível)")

