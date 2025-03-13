import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import scipy.stats as stats
import matplotlib.pyplot as plt


df = pd.read_csv("datatset_consumer_complaints.csv")

df.columns = df.columns.str.strip()

st.title("Análise Exploratória de Reclamações de Consumidores")

## **1. Apresentação dos Dados**
st.header("1️⃣ Apresentação dos Dados e Tipos de Variáveis")
st.write("""
Este conjunto de dados contém reclamações de consumidores sobre diversas empresas e setores.
Ele inclui informações como o tipo de produto, estado, canal de submissão, datas de recebimento e resolução,
tempo de resolução e resposta dentro do prazo.
""")
st.subheader("Amostra dos Dados")
st.write(df.head())
st.subheader("Tipos de Variáveis")
st.write(df.dtypes)
st.subheader("Principais Perguntas de Análise")
st.write("""
1. Qual o tempo médio de resolução das reclamações?
2. Quais os produtos mais reclamados?
3. Existe correlação entre o tempo de resposta e a contestação pelo consumidor?
4. Como os tempos de resolução estão distribuídos? Eles seguem uma distribuição normal?
""")

## **2. Medidas Estatísticas e Correlações**
st.header("2️⃣ Medidas Estatísticas e Análise Inicial dos Dados")
st.subheader("Medidas Centrais do Tempo de Resolução")
if "Resolution time(in days)" in df.columns:
   mean_time = df["Resolution time(in days)"].mean()
   median_time = df["Resolution time(in days)"].median()
   mode_time = df["Resolution time(in days)"].mode()[0]
   std_dev = df["Resolution time(in days)"].std()
   variance = df["Resolution time(in days)"].var()
   st.write(f"**Média:** {mean_time:.2f} dias")
   st.write(f"**Mediana:** {median_time:.2f} dias")
   st.write(f"**Moda:** {mode_time:.2f} dias")
   st.write(f"**Desvio Padrão:** {std_dev:.2f} dias")
   st.write(f"**Variância:** {variance:.2f} dias")
else:
   st.error("A coluna 'Resolution time(in days)' não está disponível no dataset.")
st.subheader("Distribuição do Tempo de Resolução")
fig_hist = px.histogram(df, x="Resolution time(in days)", nbins=30, title="Distribuição do Tempo de Resolução")
st.plotly_chart(fig_hist)
st.subheader("📈 Matriz de Correlação")
numeric_cols = df.select_dtypes(include=["number"]).columns
correlation_matrix = df[numeric_cols].corr()
fig_corr = px.imshow(correlation_matrix, text_auto=True, title="Matriz de Correlação")
st.plotly_chart(fig_corr)
st.write("""A matriz de correlação revela a intensidade e a direção das relações lineares entre variáveis numéricas,
com coeficientes variando de -1 a 1. Valores próximos de 1 ou -1 indicam correlações fortes, positivas ou negativas, 
respectivamente, enquanto valores próximos de 0 sugerem pouca ou nenhuma correlação linear. Na análise das reclamações
de consumidores, observar que o tempo de resolução possui uma correlação negativa com a variável “Resposta em tempo hábil” 
sugere que tempos de resolução mais longos estão associados a respostas fora do prazo. Além disso, uma correlação positiva 
entre o tempo de resolução e a variável “Reclamação contestada pelo consumidor” indica que tempos de resolução mais extensos 
podem aumentar a probabilidade de contestação por parte do consumidor. Essas correlações destacam a importância de tempos de 
rápidos para melhorar a satisfação do cliente e a conformidade com os prazos estabelecidos. """)

## **3. Aplicação de Distribuições Probabilísticas**
st.header("3️⃣ Aplicação de Distribuições Probabilísticas")

### **Distribuição Normal**
st.subheader("Distribuição Normal")
st.write("O tempo de resolução pode seguir uma distribuição normal. Vamos testar isso.")
mu, sigma = df["Resolution time(in days)"].mean(), df["Resolution time(in days)"].std()
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
pdf = stats.norm.pdf(x, mu, sigma)
fig, ax = plt.subplots()
ax.hist(df["Resolution time(in days)"], bins=30, density=True, alpha=0.6, color='g')
ax.plot(x, pdf, 'r', label="Curva Normal Teórica")
ax.set_title("Aproximação da Distribuição Normal para o Tempo de Resolução")
ax.set_xlabel("Tempo de Resolução (dias)")
ax.set_ylabel("Densidade")
st.pyplot(fig)
st.write("""
A distribuição normal é usada aqui porque queremos verificar se os tempos de resolução seguem um comportamento previsível.
Se o gráfico se aproximar da curva normal teórica, isso sugere que podemos modelar previsões futuras com base nessa distribuição.
""")

### **Distribuição de Poisson**
st.subheader("Distribuição de Poisson")
st.write("A distribuição de Poisson é útil para modelar a frequência de eventos em um intervalo de tempo.")
df["Date received"] = pd.to_datetime(df["Date received"], errors="coerce")
df["date_only"] = df["Date received"].dt.date
complaints_per_day = df.groupby("date_only").size()


lambda_poisson = complaints_per_day.mean()


x_poisson = np.arange(0, complaints_per_day.max())
poisson_dist = stats.poisson.pmf(x_poisson, lambda_poisson)
fig, ax = plt.subplots()
ax.bar(x_poisson, poisson_dist, alpha=0.6, color='b')
ax.set_title("Distribuição de Poisson - Número de Reclamações por Dia")
ax.set_xlabel("Número de Reclamações")
ax.set_ylabel("Probabilidade")
st.pyplot(fig)
st.write(f"""
A média de reclamações por dia é de **{lambda_poisson:.2f}**. Isso sugere que o número de reclamações pode ser modelado
com uma distribuição de Poisson, útil para prever a frequência de novas reclamações em períodos futuros. A distribuição 
obtida mostra que a maioria dos dias apresenta um volume de reclamações próximo à média, com variações ocasionais que 
podem estar associadas a fatores externos, como sazonalidade ou eventos específicos. Observa-se uma assimetria na 
distribuição, indicando a ocorrência de dias atípicos com um número significativamente maior de reclamações. Esses picos 
sugerem a necessidade de estratégias operacionais para lidar com períodos de alta demanda, garantindo maior eficiência no
atendimento. Além disso, a modelagem permite estimar a probabilidade de diferentes volumes de reclamações, auxiliando no 
planejamento e na alocação de recursos.
""")


st.header("Conclusões")
st.write("""
- A maior parte das reclamações é resolvida rapidamente, mas há uma dispersão significativa nos tempos de resolução.
- Algumas variáveis possuem correlação fraca, indicando que outros fatores podem influenciar a contestação pelo consumidor.
- O tempo de resolução se aproxima de uma distribuição normal, mas há desvios.
- A distribuição de Poisson ajuda a modelar a quantidade de reclamações por dia, sendo útil para previsões operacionais.
""")
