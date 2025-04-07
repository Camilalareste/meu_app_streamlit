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

# Criar mapa com folium
m = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

# Simulação de dados
onibus = [
    {"linha": "101", "lat": -8.047, "lon": -34.88},
    {"linha": "102", "lat": -8.05, "lon": -34.87},
    {"linha": "103", "lat": -8.045, "lon": -34.875},
]

metro = [
    {"estacao": "Central", "lat": -8.049, "lon": -34.876},
    {"estacao": "Sul", "lat": -8.055, "lon": -34.873},
]

acidentes = [
    {"local": "Av. Norte", "lat": -8.048, "lon": -34.872, "descricao": "Colisão leve"},
]

lixo = [
    {"bairro": "Boa Vista", "lat": -8.043, "lon": -34.879, "horario": "06:00 - 08:00"},
    {"bairro": "Casa Forte", "lat": -8.032, "lon": -34.915, "horario": "08:00 - 10:00"},
]

escolar = [
    {"escola": "Escola A", "lat": -8.041, "lon": -34.881},
    {"escola": "Escola B", "lat": -8.044, "lon": -34.885},
]

# Adicionar marcadores ao mapa
for o in onibus:
    folium.Marker([o["lat"], o["lon"]], tooltip=f"Ônibus linha {o['linha']}", icon=folium.Icon(color='blue', icon='bus', prefix='fa')).add_to(m)

for mtr in metro:
    folium.Marker([mtr["lat"], mtr["lon"]], tooltip=f"Estação {mtr['estacao']}", icon=folium.Icon(color='green', icon='train', prefix='fa')).add_to(m)

for a in acidentes:
    folium.Marker([a["lat"], a["lon"]], tooltip=f"🚨 Acidente: {a['descricao']}", icon=folium.Icon(color='red', icon='exclamation-triangle', prefix='fa')).add_to(m)

for l in lixo:
    folium.Marker([l["lat"], l["lon"]], tooltip=f"🗑️ {l['bairro']} - Coleta: {l['horario']}", icon=folium.Icon(color='gray', icon='trash', prefix='fa')).add_to(m)

for e in escolar:
    folium.Marker([e["lat"], e["lon"]], tooltip=f"🎒 {e['escola']} - Transporte escolar", icon=folium.Icon(color='purple', icon='school', prefix='fa')).add_to(m)

# Interface para modo de visualização
modo = st.sidebar.selectbox("Escolha o modo de visualização:", ["Usuário", "Gestor"])

if modo == "Usuário":
    st.subheader("👤 Modo Usuário")
    st.markdown("Visualize onde estão os ônibus, metrô e acidentes próximos em tempo real.")
    st.markdown("Também veja a programação de coleta de lixo e escolas atendidas.")

elif modo == "Gestor":
    st.subheader("🧑‍💼 Modo Gestor")
    st.markdown("Painel interativo com visão ampla da mobilidade urbana.")
    st.markdown("Use os dados para tomar decisões estratégicas em tempo real.")
    st.metric("Total de Ônibus Ativos", len(onibus))
    st.metric("Ocorrências Atuais", len(acidentes))
    st.metric("Zonas de Coleta de Lixo", len(lixo))

# Exibir o mapa
folium_static(m)

st.caption(f"Atualizado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
folium_static(m)




