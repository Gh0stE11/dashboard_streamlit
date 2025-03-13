import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

if "data" not in st.session_state:
    df = pd.read_csv("datatset_consumer_complaints.csv")
    st.session_state["data"] = df

df = st.session_state["data"]

# Configuração da página
st.sidebar.markdown("Desenvolvido por Caio Hideki")

# Adicionando logo com streamlit-extras
# add_logo("logo.jpeg")

# Adicionando o logo
st.logo("pngegg.png")

# Adicionando o logo no body
st.image("Image.jpg", width=150)

st.title('Caio Hideki Cardenas Ishizu | Engenharia de Software')

st.header('Apresentação')

st.write('Tendo como principal objetivo ganhar experiência no mercado de trabalho de forma honesta e respeitosa com todos. Sempre em busca'
'de conhecimento e aprendizado. Aprendendo linguagens de programação (Python, HTML, CSS, Javascript, C...). Possuo experiêcia com programas da Adobe'
', edição de vídeo, programas Office e Inglês Fluente')


