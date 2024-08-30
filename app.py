# app.py

'''Archivo que ejecuta aplicación web proyecto sprint 6'''

import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Aplicación web proyecto sprint 6')

st.write('Esta aplicación proporciona información sobre automóviles')

car_data = pd.read_csv(
    'C:\\Users\\usuario\\OneDrive\\Data analysis\\Bootcamp\\Sprint6\\project\\project_s6\\vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Creación de gráfico de dispersión
disp_button = st.button('Construir gráfico dispersión')  # crear un botón

if disp_button:
    st.write('Creación de un gráfico de dispersión para el conunto de datos de anuncios de venta de coches')
    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price")
    fig2.show()  # crear gráfico de dispersión
    st.plotly_chart(fig2)
