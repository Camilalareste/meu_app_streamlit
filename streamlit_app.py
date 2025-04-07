import streamlit as st
import folium
from streamlit_folium import folium_static
import random
from datetime import datetime

st.set_page_config(page_title="Transporte Inteligente", layout="wide")

# Adiciona a logo e informações da startup
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://drive.google.com/uc?export=view&id=1qMZNjnCYmlwWBS840AWsDrHTsdUgNk7c", width=120)
with col2:
    st.markdown("""
        ### Plataforma de Mobilidade Urbana Inteligente
        **CNPJ:** 60.262.825/0001-06  
        **Contato:** +55 81 99505-5354  
        **Email:** camilalareste@xyzlogicflow.tech
    """)

# Opção de visualização
modo = st.selectbox("👥 Escolha seu perfil de acesso:", ["Usuário", "Gestor", "Emergência"])

# Localização base
latitude_base = -8.0476
longitude_base = -34.8770

# Criar mapa base
m = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)

# Simulação de dados
onibus = [
    {"linha": "101", "lat": -8.047, "lon": -34.88},
    {"linha": "102", "lat": -8.05, "lon": -34.87},
    {"linha": "103", "lat": -8.045, "lon": -34.875}
]

metro = [
    {"estacao": "Joana Bezerra", "lat": -8.060, "lon": -34.872},
    {"estacao": "Recife", "lat": -8.063, "lon": -34.870}
]

coleta_lixo = [
    {"rota": "Centro", "lat": -8.048, "lon": -34.876},
    {"rota": "Boa Viagem", "lat": -8.110, "lon": -34.880}
]

escolar = [
    {"rota": "Municipal", "lat": -8.052, "lon": -34.870},
    {"rota": "Rural", "lat": -8.095, "lon": -34.865}
]

emergencia = [
    {"tipo": "Ambulância", "lat": -8.049, "lon": -34.874},
    {"tipo": "Bombeiro", "lat": -8.059, "lon": -34.879}
]

acidentes = [
    {"tipo": "Colisão", "lat": -8.051, "lon": -34.873},
    {"tipo": "Alagamento", "lat": -8.057, "lon": -34.878}
]

# Adiciona marcadores
for o in onibus:
    folium.Marker([o["lat"], o["lon"]], tooltip=f"Ônibus Linha {o['linha']}", icon=folium.Icon(color="blue", icon="bus", prefix="fa")).add_to(m)

for mtr in metro:
    folium.Marker([mtr["lat"], mtr["lon"]], tooltip=f"Metrô - {mtr['estacao']}", icon=folium.Icon(color="green", icon="train", prefix="fa")).add_to(m)

for l in coleta_lixo:
    folium.Marker([l["lat"], l["lon"]], tooltip=f"Coleta de Lixo - {l['rota']}", icon=folium.Icon(color="darkgreen", icon="trash", prefix="fa")).add_to(m)

for e in escolar:
    folium.Marker([e["lat"], e["lon"]], tooltip=f"Ônibus Escolar - {e['rota']}", icon=folium.Icon(color="orange", icon="graduation-cap", prefix="fa")).add_to(m)

for em in emergencia:
    folium.Marker([em["lat"], em["lon"]], tooltip=f"Emergência - {em['tipo']}", icon=folium.Icon(color="red", icon="plus", prefix="fa")).add_to(m)

for a in acidentes:
    folium.Marker([a["lat"], a["lon"]], tooltip=f"⚠️ Acidente: {a['tipo']}", icon=folium.Icon(color="lightgray", icon="exclamation-triangle", prefix="fa")).add_to(m)

# Exibe o mapa
folium_static(m)

# Indicadores (simulados)
st.sidebar.header("📊 Indicadores em Tempo Real")
st.sidebar.metric("Ônibus em Operação", len(onibus))
st.sidebar.metric("Acidentes Reportados", len(acidentes))
st.sidebar.metric("Coletas de Lixo Ativas", len(coleta_lixo))
st.sidebar.metric("Emergências em Curso", len(emergencia))
st.sidebar.metric("Conexões Metrô-Ônibus", 5)
st.sidebar.metric("Redução de CO₂", f"{round(random.uniform(5.0, 15.0), 2)} toneladas")

# Rodapé com timestamp
st.caption(f"Atualizado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
st.caption("Startup: VaiFácil + XYZ LogicFlow")





