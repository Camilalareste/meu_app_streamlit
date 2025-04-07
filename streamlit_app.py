import streamlit as st
import folium
from streamlit_folium import folium_static
import random
from datetime import datetime

st.set_page_config(page_title="Transporte Inteligente", layout="wide")
st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Base de localização (Recife)
latitude_base = -8.0476
longitude_base = -34.8770

# Criar mapa
m = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

# Dados simulados de ônibus
onibus = [
    {"linha": "101", "lat": -8.047, "lon": -34.88},
    {"linha": "102", "lat": -8.05, "lon": -34.87},
    {"linha": "103", "lat": -8.045, "lon": -34.875}
]

# Dados simulados de metrô
metro = [
    {"estacao": "Estação Central", "lat": -8.045, "lon": -34.88},
    {"estacao": "Estação Sul", "lat": -8.05, "lon": -34.885}
]

# Dados simulados de acidentes
acidentes = [
    {"local": "Av. Conde da Boa Vista", "lat": -8.048, "lon": -34.881, "hora": datetime.now().strftime('%H:%M')}
]

# Dados de lixo e ônibus escolar
lixo = {"lat": -8.049, "lon": -34.879, "proxima_coleta": "08:00"}
escolar = [
    {"escola": "Escola A", "lat": -8.046, "lon": -34.878},
    {"escola": "Escola B", "lat": -8.044, "lon": -34.876}
]

# Zona Azul e estacionamento
estacionamentos = [
    {"nome": "Zona Azul 1", "lat": -8.043, "lon": -34.879},
    {"nome": "Estacionamento Central", "lat": -8.045, "lon": -34.882}
]

# Adiciona ícones no mapa
for o in onibus:
    folium.Marker(
        [o["lat"], o["lon"]],
        popup=f"Ônibus Linha {o['linha']}",
        icon=folium.Icon(color="blue", icon="bus", prefix="fa")
    ).add_to(m)

for mtr in metro:
    folium.Marker(
        [mtr["lat"], mtr["lon"]],
        popup=f"Estação de Metrô: {mtr['estacao']}",
        icon=folium.Icon(color="green", icon="train", prefix="fa")
    ).add_to(m)

for ac in acidentes:
    folium.Marker(
        [ac["lat"], ac["lon"]],
        popup=f"🚧 Acidente: {ac['local']} às {ac['hora']}",
        icon=folium.Icon(color="red", icon="exclamation-triangle", prefix="fa")
    ).add_to(m)

folium.Marker(
    [lixo["lat"], lixo["lon"]],
    popup=f"🚛 Próxima coleta de lixo: {lixo['proxima_coleta']}",
    icon=folium.Icon(color="orange", icon="trash", prefix="fa")
).add_to(m)

for e in escolar:
    folium.Marker(
        [e["lat"], e["lon"]],
        popup=f"🚌 Ônibus Escolar - {e['escola']}",
        icon=folium.Icon(color="purple", icon="graduation-cap", prefix="fa")
    ).add_to(m)

for est in estacionamentos:
    folium.Marker(
        [est["lat"], est["lon"]],
        popup=f"🅿️ {est['nome']}",
        icon=folium.Icon(color="cadetblue", icon="car", prefix="fa")
    ).add_to(m)

# Interface para escolher visualização
modo = st.sidebar.selectbox("Modo de Visualização", ["Usuário", "Gestor"])

if modo == "Usuário":
    st.sidebar.success("👤 Modo Usuário Ativo")
    st.markdown("Veja informações úteis de transporte ao seu redor.")
else:
    st.sidebar.success("🛠️ Modo Gestor Ativo")
    st.markdown("Monitore o trânsito, coletas e eventos urbanos em tempo real.")

# Exibir mapa
folium_static(m)




