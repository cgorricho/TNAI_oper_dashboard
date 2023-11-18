### TERMONORTE - PROYECTO DE INTELIGENCIA ARTIFICIAL ###
#
# Archivo base para webapp Prototipo
# Dashboard de Operaciones: Informe de Parámetros
# Lider funcional: Daniel Amaya
#
# Desarrollado por:
# HEPTAGON GenAI | AIML
# Carlos Gorricho
# cel: +57 314 771 0660
# email: cgorricho@heptagongroup.co
#

### IMPORTAR DEPENDENCIAS ###
import streamlit as st        # web development
import numpy as np            # np mean, np random 
import pandas as pd           # read csv, df manipulation
import time                   # to simulate a real time data, time loop 
import plotly.express as px   # interactive charts
import matplotlib.pyplot as plt
import seaborn as sns         # seaborn graphing library
import regex                  # regular expresions para limpiar texto


### IMPORTA Y PREPARA DATOS ###
# crea archivo de excel como fuente de datos para pandas
xls = pd.ExcelFile(r'Copia de Parámetros Termonorte  año 2023.xlsx')

# importa información de la hoja 
df_datos = pd.read_excel(
    xls,                   # archivo de excel
    sheet_name='Datos',    # pestaña
    nrows=365,             # número de filas a importar
    )

# limpia nombres de columnas
new_cols = []
for col in df_datos.columns:
    new_col = regex.sub("\\n", '', col).strip()
    new_cols.append(new_col)

# reemplaza datos en el dataframe
df_datos.columns = new_cols

# reemplaza columna mes
df_datos['Mes'] = df_datos['Fecha'].dt.month

# reemplaza índice
df_datos = df_datos.set_index('Fecha')





### DEFINICION DE LA PAGINA ###

# Configuración de la página
st.set_page_config(
    page_title = 'TERMONORTE',
    # page_icon = '🏭',
    layout = 'wide'
)

# barra lateral
st.sidebar.image("logo_TN_small.png")
with st.sidebar:
    mes = st.slider('mes', min_value=1, max_value=12, value=1, step=1)

st.sidebar.write(f'Mes inicial: {mes}')


# crea layout para el encabezado
col1, col2 = st.columns([1, 5])

with col1:
   st.image("logo_TN_small.png")

with col2:
   st.header('Informe de Parámetros')


# pestañas para el reporte
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
   ["Despachos", 
    "Consumos",
    "Oferta",
    "Parámetros",
    "Ind. Ambientales",
    "Operación",
    "Datos (PROVISIONAL)"])

# crea datos aleatorios
data = np.random.randn(10, 1)


# ingresa información para cada pestaña
with tab1:
   # mes = 2

   datos_graf = df_datos[df_datos.Mes == mes]

   fig, ax = plt.subplots(figsize=(10,5))
   ax.plot(datos_graf.index, datos_graf['D. XM[MWh]'], label='XM (MWH)')
   ax.plot(datos_graf.index, datos_graf['DPI [MWh]'], label='Preideal (MWH)')
   ax.plot(datos_graf.index, datos_graf['DN [MWh]'], label='Nacional (MWH)')
   ax.plot(datos_graf.index, datos_graf['DP [MWh]'], label='Programado (MWH)')
   ax.legend()

   st.pyplot(fig)

with tab2:
   mes = 2

   datos_graf = df_datos[df_datos.Mes == mes]

   fig, ax = plt.subplots(figsize=(10,5))
   ax.plot(datos_graf.index, datos_graf['D. XM[MWh]'], label='XM (MWH)')
   ax.plot(datos_graf.index, datos_graf['DPI [MWh]'], label='Preideal (MWH)')
   ax.plot(datos_graf.index, datos_graf['DN [MWh]'], label='Nacional (MWH)')
   ax.plot(datos_graf.index, datos_graf['DP [MWh]'], label='Programado (MWH)')
   ax.legend()

   st.pyplot(fig)

with tab3:
   st.header("An owl")
   st.line_chart(data)

with tab7:
   st.header("Datos tomados de archivo de Excel")
   st.write(df_datos)
   



