import streamlit as st
import folium
from streamlit_folium import folium_static
import random

st.set_page_config(page_title="Transporte Inteligente", layout="wide")
st.title("🚍 Mapa Inteligente de Transporte Público")

# Base de localização (ex: Recife)
latitude_base = -8.0476
longitude_base = -34.8770

# Criar mapa com folium
m = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

# Dados simulados de ônibus
onibus = [
    {"linha": "101", "lat": -8.047, "lon": -34.88},
    {"linha": "102", "lat": -8.05, "lon": -34.87},
    {"linha": "103", "lat": -8.045, "lon": -34.875},
]

# Adiciona marcadores de ônibus no mapa
for o in onibus:
    folium.Marker(
        location=[o["lat"], o["lon"]],
        popup=f"Linha {o['linha']}",
        icon=folium.Icon(color="blue", icon="bus", prefix='fa')
    ).add_to(m)

# Exibir mapa no Streamlit
folium_static(m)
import streamlit as st
import folium
from streamlit_folium import folium_static
import random

# Configurações da página
st.set_page_config(page_title="Transporte Inteligente", layout="wide")
st.title("🚍 Mapa Inteligente de Transporte Público")

# Base de localização (ex: Recife ou SP)
latitude_base = -8.0476  # Recife: -8.0476 | SP: -23.5505
longitude_base = -34.8770  # Recife: -34.8770 | SP: -46.6333

# Criar mapa com folium
m = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

# Dados simulados de ônibus
onibus = [
    {"linha": "101", "lat": latitude_base + random.uniform(-0.01, 0.01), "lon": longitude_base + random.uniform(-0.01, 0.01)},
    {"linha": "102", "lat": latitude_base + random.uniform(-0.01, 0.01), "lon": longitude_base + random.uniform(-0.01, 0.01)},
    {"linha": "103", "lat": latitude_base + random.uniform(-0.01, 0.01), "lon": longitude_base + random.uniform(-0.01, 0.01)},
]

# Adiciona marcadores dos ônibus no mapa
for o in onibus:
    folium.Marker(
        location=[o["lat"], o["lon"]],
        popup=f"Linha {o['linha']}",
        icon=folium.Icon(color="blue", icon="bus", prefix="fa")
    ).add_to(m)

# Exibir o mapa no Streamlit
folium_static(m)



