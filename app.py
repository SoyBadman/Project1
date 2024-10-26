import pandas as pd
import plotly.express as px
import streamlit as st

# Configurar el titulo de la página
st.header('Análisis de Datos de Vehículos 🚗')

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear dos columnas para los botones
col1, col2 = st.columns(2)

with col1:
    # Boton para el histograma
    hist_button = st.button('Mostrar Histograma de Kilometraje')

    if hist_button:
        st.write('### Distribución del Kilometraje de los Vehículos')

        # Crear un histograma
        fig_hist = px.histogram(
            car_data,
            x="odometer",
            nbins=50,
            title="Distribución del Kilometraje",
            labels={'odometer': 'Kilometraje', 'count': 'Frecuencia'}
        )

        # Mostrar el grafico
        st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    # Botón para el grafico de dispersion
    scatter_button = st.button('Mostrar Gráfico de Precio vs Kilometraje')

    if scatter_button:
        st.write('### Relación entre Precio y Kilometraje')

        # Crear un grafico de dispersion
        fig_scatter = px.scatter(
            car_data,
            x="odometer",
            y="price",
            title="Precio vs Kilometraje",
            labels={'odometer': 'Kilometraje', 'price': 'Precio ($)'}
        )

        # Mostrar el grafico
        st.plotly_chart(fig_scatter, use_container_width=True)

# Agregar informacion adicional
st.write('### Acerca de este Dashboard')
st.write('''
Este dashboard permite explorar la relación entre diferentes variables de los vehículos en venta.
- Utiliza el botón de Histograma para ver la distribución del kilometraje
- Utiliza el botón de Dispersión para ver la relación entre precio y kilometraje
''')
