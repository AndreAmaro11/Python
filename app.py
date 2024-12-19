import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.logo("images/splat.png")


df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books =  pd.read_csv("datasets/Top-100 Trending Books.csv")


price_min = df_top100_books["book price"].min()
price_max = df_top100_books["book price"].max()
ano_min = df_top100_books["year of publication"].min()
ano_max = df_top100_books["year of publication"].max()


max_price = st.sidebar.slider("Valores", price_min, price_max, price_max)
ano_filtro = st.sidebar.slider("Ano", ano_min, ano_max, ano_max)

df_books = df_top100_books[
    (df_top100_books["book price"] <= max_price) & (df_top100_books["year of publication"] <= ano_filtro)]

#graficos
st.logo("images/splat.png")

st.markdown(
    """
    <h1 style="text-align: center;">Análise da Amazon</h1>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h1 style="text-align: center;">Inicio em Python para usuário zé ruela</h1>
    """,
    unsafe_allow_html=True
)



st.divider()
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])


col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
df_reviews

st.divider()

df_books
