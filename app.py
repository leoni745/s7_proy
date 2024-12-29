import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
car_data = pd.read_csv('/home/tripleten/Documents/Proy_S7/s7_proy/vehicles_us.csv')

# Agregar un encabezado a la aplicación
st.header("Análisis de Vehículos Usados")

#######################################################################
# Crear un botón para generar el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    st.write('Creando un histograma para el conjunto de datos de anuncios de venta de coches')  # Mensaje
    
    # Crear el histograma con Plotly Express
    fig = px.histogram(car_data, x="odometer", title="Histograma de Kilometraje")
    
    # Mostrar el gráfico interactivo con Streamlit
    st.plotly_chart(fig, use_container_width=True)

#######################################################################
# Crear un botón para generar el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Al hacer clic en el botón
    st.write('Creando un gráfico de dispersión entre Kilometraje y Precio')  # Mensaje
    
    # Crear el gráfico de dispersión con Plotly Express
    fig = px.scatter(car_data, x='odometer', y='price', title="Relación entre Kilometraje y Precio")
    
    # Mostrar el gráfico interactivo con Streamlit
    st.plotly_chart(fig, use_container_width=True)

######################################################################
# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # Si la casilla está seleccionada
    st.write('Construyendo un histograma para la columna odómetro')
    
    # Crear el histograma
    fig = px.histogram(car_data, x="odometer", title="Histograma de Kilometraje")
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:  # Si la casilla está seleccionada
    st.write('Construyendo gráfico de dispersión entre Kilometraje y Precio')
    
    # Crear el gráfico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price', title="Relación entre Kilometraje y Precio")
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
    

