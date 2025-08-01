import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')
st.header("Cuadro de Mandos Interactivo")

st.write("Vista previa de los datos:")
st.dataframe(df.head())

st.subheader("Histograma")
if st.button("Mostrar Histograma"):
    col_hist = st.selectbox("Selecciona la columna para el histograma:", df.select_dtypes(include=['float64', 'int64']).columns)
    fig_hist = px.histogram(df, x=col_hist, nbins=30, title=f"Histograma de {col_hist}")
    st.plotly_chart(fig_hist)

    st.subheader("Gráfico de Dispersión")
if st.button("Mostrar Dispersión"):
    col_x = st.selectbox("Eje X:", df.select_dtypes(include=['float64', 'int64']).columns, key="x")
    col_y = st.selectbox("Eje Y:", df.select_dtypes(include=['float64', 'int64']).columns, key="y")
    fig_scatter = px.scatter(df, x=col_x, y=col_y, title=f"Gráfico de Dispersión: {col_x} vs {col_y}")
    st.plotly_chart(fig_scatter)