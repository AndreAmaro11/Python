import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.logo("images/splat.png")

#cabeçalho
st.markdown(
    """
    <h1 style="text-align: center;">Horas de Automação de Processos</h1>
    """,
    unsafe_allow_html=True
    )
#dados
dados_excel = pd.read_excel("datasets/dados_horas_estudo.xlsx")
#Filtro
filtrosetor = dados_excel["Setor"].unique()
filtroAno = dados_excel["Ano"].unique()
#filtroprocesso = dados_excel["Processo"].unique()

#VariavelFiltro
filtro_setor = st.sidebar.selectbox("Setor",filtrosetor)
filtro_ano = st.sidebar.selectbox("Ano",filtroAno)
#filtro_processo = st.sidebar.selectbox("Processo",filtroprocesso)
#SomaGraficos
somacolunatotal = dados_excel["Total Horas"].sum()
somacoluna_rh = dados_excel[(dados_excel["Setor"] == "RH") & (dados_excel["Ano"] == filtro_ano)]["Total Horas"].sum()

somacoluna_financeiro = dados_excel[dados_excel["Setor"] == "Financeiro"]["Total Horas"].sum()
somacoluna_contabilidade = dados_excel[dados_excel["Setor"] == "Contabilidade"]["Total Horas"].sum()
somacoluna_engenharia = dados_excel[dados_excel["Setor"] == "Engenharia"]["Total Horas"].sum()
somacoluna_sms = dados_excel[dados_excel["Setor"] == "SMS"]["Total Horas"].sum()
somacoluna_suprimentos = dados_excel[dados_excel["Setor"] == "Suprimentos"]["Total Horas"].sum()
somacoluna_ti = dados_excel[dados_excel["Setor"] == "TI"]["Total Horas"].sum()

dados_excel = dados_excel[(dados_excel["Setor"] == filtro_setor) &  (dados_excel["Ano"] == filtro_ano)]

#Graficos
fig1 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = somacolunatotal,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Total"},
    gauge={
        'bar': {'color': "blue"},  # Cor da barra
        'axis': {'range': [0, 10000]},  # Ajuste o intervalo do medidor
        'steps': [
            {'range': [0, 5000], 'color': "lightgray"},  # Cor de fundo para o intervalo 0-50
            {'range': [1000, 10000], 'color': "gray"}     # Cor de fundo para o intervalo 50-100
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 1000  # Altere o valor do limite para destacar
        }
    }
))
fig2 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = somacoluna_financeiro,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Financeiro"}))

fig3 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = somacoluna_rh,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "RH"}))

fig4 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = somacoluna_ti,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "TI"}))

fig5 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = somacoluna_suprimentos,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Suprimentos"}))

fig6 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = somacoluna_contabilidade,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Contabilidade"}))

fig7 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = somacoluna_engenharia,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Engenharia"}))

fig8 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = somacoluna_sms,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "SMS"}))



col1, col2, col3 = st.columns(3)
col1.plotly_chart(fig1)
col2.plotly_chart(fig2)
col3.plotly_chart(fig3)

col3, col4, col5 = st.columns(3)
col3.plotly_chart(fig4)
col4.plotly_chart(fig5)
col5.plotly_chart(fig6)

col7, col8, col9 = st.columns(3)
col7.plotly_chart(fig7)
col8.plotly_chart(fig8)

dados_excel
