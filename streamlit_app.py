import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import random
import googlemaps
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Plataforma de Mobilidade Urbana", layout="wide")

# Título
st.title("🚦 Plataforma de Mobilidade Urbana Inteligente")

# Sidebar: Modo de Visualização
modo = st.sidebar.radio("👤 Modo de Visualização", ["Usuário", "Gestor"])

# Coordenadas Base (Recife)
latitude_base = -8.0476
longitude_base = -34.8770

# Função para adicionar ícones ao mapa
def adicionar_icones(mapa, dados=None):  
    icones = {
        "Lixo": {"icone": "trash", "cor": "green"},
        "Trânsito": {"icone": "car", "cor": "red"},
        "Metrô": {"icone": "train", "cor": "purple"},
        "Zona Azul": {"icone": "info-sign", "cor": "blue"},
        "Acidente": {"icone": "exclamation-sign", "cor": "orange"},
    }

    if dados is not None:
        for _, row in dados.iterrows():
            tipo = row.get("tipo", "Desconhecido")
            lat = row.get("latitude", latitude_base)
            lon = row.get("longitude", longitude_base)
            
            if tipo in icones:
                folium.Marker(
                    location=[lat, lon],
                    popup=tipo,
                    icon=folium.Icon(color=icones[tipo]["cor"], 
                                     icon=icones[tipo]["icone"], 
                                     prefix='glyphicon')
                ).add_to(mapa)
    else:
        for i in range(15):
            tipo = random.choice(list(icones.keys()))
            lat_offset = random.uniform(-0.01, 0.01)
            lon_offset = random.uniform(-0.01, 0.01)
            folium.Marker(
                location=[latitude_base + lat_offset, longitude_base + lon_offset],
                popup=f"{tipo} #{i+1}",
                icon=folium.Icon(color=icones[tipo]["cor"], 
                                 icon=icones[tipo]["icone"], 
                                 prefix='glyphicon')
            ).add_to(mapa)

# Modo Usuário
if modo == "Usuário":
    aba = st.sidebar.radio("Menu do Usuário", (
        "Google Maps",
        "Chatbot",
        "Paradas",
        "Origem e Destino",
        "Alertas"
    ))

    if aba == "Google Maps":
        st.subheader("🌍 Visualização com Google Maps")
        
        # Solicitar chave da API do Google Maps
        gmaps_key = st.text_input("Insira sua chave da API do Google Maps:")
        if gmaps_key:
            gmaps = googlemaps.Client(key=gmaps_key)

            # Entrada de localização
            endereco = st.text_input("Digite um endereço ou localização:")

            if st.button("Buscar Localização"):
                try:
                    # Geocodificar o endereço
                    geocode_result = gmaps.geocode(endereco)
                    if geocode_result:
                        location = geocode_result[0]['geometry']['location']
                        lat, lng = location['lat'], location['lng']

                        # Exibir o mapa com a localização
                        mapa = folium.Map(location=[lat, lng], zoom_start=15)
                        folium.Marker([lat, lng], popup=endereco).add_to(mapa)
                        folium_static(mapa)
                    else:
                        st.error("Localização não encontrada.")
                except Exception as e:
                    st.error(f"Erro na API do Google Maps: {e}")

    elif aba == "Chatbot":
        st.subheader("🤖 Chatbot")
        user_input = st.text_input("Digite sua pergunta para o chatbot:")
        if st.button("Enviar"):
            try:
                # Simulação de resposta (substitua pelo modelo ou API do OpenAI)
                resposta = f"Você perguntou: '{user_input}'. Resposta automática: 'Estou aqui para ajudar!'"
                st.write(resposta)
            except Exception as e:
                st.error(f"Erro ao processar a mensagem: {e}")

    elif aba == "Paradas":
        st.subheader("📍 Paradas Próximas")
        st.markdown("Funcionalidade em desenvolvimento.")

    elif aba == "Origem e Destino":
        st.subheader("📍 Origem e Destino")
        origem = st.text_input("Digite sua origem:")
        destino = st.text_input("Digite seu destino:")
        if st.button("Calcular Rota"):
            st.markdown("Funcionalidade de cálculo de rota em desenvolvimento.")

    elif aba == "Alertas":
        st.subheader("🚨 Alertas em Tempo Real")
        st.markdown("Funcionalidade em desenvolvimento.")

# Modo Gestor
elif modo == "Gestor":
    aba = st.sidebar.radio("Menu do Gestor", (
        "Mapa Interativo",
        "Ocorrências 156",
        "Carregar Arquivo (Excel/CSV)",
        "Informações dos Usuários"
    ))

    if aba == "Mapa Interativo":
        st.subheader("🌍 Mapa Interativo")
        mapa = folium.Map(location=[latitude_base, longitude_base], zoom_start=13)
        adicionar_icones(mapa)
        folium_static(mapa)

    elif aba == "Ocorrências 156":
        st.subheader("Ocorrências 156")
        st.markdown("Funcionalidade em desenvolvimento.")

    elif aba == "Carregar Arquivo (Excel/CSV)":
        st.subheader("📂 Carregar Arquivo Excel ou CSV")
        uploaded_file = st.file_uploader("Faça o upload do arquivo", type=["csv", "xlsx"])
        if uploaded_file is not None:
            try:
                # Detecta se é Excel ou CSV
                if uploaded_file.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_file)
                elif uploaded_file.name.endswith(".xlsx"):
                    df = pd.read_excel(uploaded_file)

                st.write("Pré-visualização dos Dados:")
                st.dataframe(df)

                # Salvar como CSV (se necessário)
                if st.button("Salvar como CSV"):
                    df.to_csv("dados_convertidos.csv", index=False)
                    st.success("Arquivo salvo como 'dados_convertidos.csv'")
            except Exception as e:
                st.error(f"Erro ao processar o arquivo: {e}")

    elif aba == "Informações dos Usuários":
        st.subheader("📊 Informações dos Usuários")
        st.markdown("Funcionalidade para listar usuários e gerenciar dados em desenvolvimento.")
        Atualizando última linha do streamlit_app.py
        git add streamlit_app.py
git commit -m "Atualizando última linha do streamlit_app.py"
git push
!pip install streamlit
!streamlit run streamlit_app.py & npx localtunnel --port 8501
%cd meu_app_streamlit


