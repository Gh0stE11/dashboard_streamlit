import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

import streamlit as st

# Configuração da página
st.set_page_config(page_title="Formação e Experiência", layout="wide")

# Configuração da página
st.sidebar.markdown("Desenvolvido por Caio Hideki")

# Adicionando logo com streamlit-extras
# add_logo("logo.jpeg")

# Adicionando o logo
st.logo("pngegg.png")

# Adicionando o logo no body

st.title('Formação e Experiência')

st.header('Formação')

st.write('- Conclusão do Ensino Médio - Colégio Guilherme de Almeida (2006 - 2021)')
st.write('- Cursando Engenharia de Software - FIAP (2023 - 2027)')

st.header('Conhecimentos')

st.subheader('Conhecimentos de Idiomas')
st.write('- Libras Básico')
st.write('- Português Nativo') 
st.write('- Inglês Avançado')
st.write('- Espanhol Básico') 

st.subheader('Conhecimentos de Informática')
st.write('- Power BI')
st.write('- Python Intermediário')
st.write('- Web Design Intermediário')
st.write('- Power Point Intermediário') 
st.write('- MySQL Básico') 
st.write('- JavaScript Intermediário') 
st.write('- HTML Intermediário')
st.write('- Excel Avançado')
st.write('- CSS Intermediário')
st.write('- C/C++ Básico')
st.write('- Access Básico')

