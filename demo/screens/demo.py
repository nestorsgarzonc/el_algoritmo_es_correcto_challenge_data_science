from ai.model import ModelData, XGBoost
from geo_data import GeoLocation
import streamlit as st
import pandas as pd


geoClient = GeoLocation()


def demo():
    st.title('Demo 👽')

    st.text(
        'Llena los siguientes datos para darte el precio de la vivienda y el precio/area')

    """
    'area', 'banos', 'estrato', 'garajes', 'habitaciones', 'piso',
    'valoradministracion', 'latitud', 'longitud', '0-1 anos', '1-10 anos',
    '10-30 anos', '30 anos', 'tiponegocio_Arriendo', 'tiponegocio_Venta',
    'tiponegocio_Venta Y Arriendo', 'tipoinmueble_Casa',
    'tipoinmueble_Apartamento'
    """
    col1, col2 = st.beta_columns(2)
    area = col1.number_input(
        '¿Cuál es el área de tu inmueble?', min_value=0, step=1, format='%d')
    banos = col2.number_input(
        '¿Cuántos baños tiene?',
        min_value=0,  step=1, format='%d')
    garajes = col1.number_input(
        '¿Cuántos garajes tiene tu inmueble?', min_value=0,  step=1, format='%d')
    habitaciones = col2.number_input(
        '¿Cuántas habitaciones tiene?', min_value=0,  step=1, format='%d')
    piso = col1.number_input(
        '¿Cuántos pisos tiene tu casa?', min_value=0,  step=1, format='%d')
    estrato = col1.number_input(
        '¿Cual es el estrato? (Valor minimo: 1)', min_value=1,
        step=1, format='%d'
    )
    valoradministracion = col2.number_input(
        '¿Cuánto pagas de administración? (Si no aplica deja en 0)', min_value=0,
        step=1, format='%d'
    )
    valorVivienda = col2.number_input(
        '¿Cuánto crees que cuesta tu casa?', min_value=0,
        step=1, format='%d'
    )

    street = st.text_input("Dirección", "Cra 76 sur # 57-96 ")
    city = st.text_input("Ciudad", "Bogota")
    country = "Colombia"

    location = geoClient.get_cords(f'{street}, {city}, {country}')
    lat = location.lat
    lon = location.lng
    map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    st.map(map_data, zoom=14)
    tiempo_de_construido = st.slider(
        '¿Cuánto años tiene de construido tu inmueble?', min_value=0, max_value=30, value=0, step=1
    )
    tipo_negocio = st.radio('¿Qué tipo de negocio se puede haer con la inmueble?',
                            ('Sólo Venta', 'Arriendo y Venta', 'Sólo Arriendo'))
    tipo_inmueble = st.radio(
        '¿Qué tipo de inmueble es?', ('Casa', 'Apartamento')
    )

    if st.button('Predecir'):
        data = ModelData(
            area=area,
            banos=banos,
            garajes=garajes,
            habitaciones=habitaciones,
            piso=piso,
            estrato=estrato,
            valoradministracion=valoradministracion,
            valorventa=valorVivienda,
            latitud=lat,
            longitud=lon,
        )
        if tipo_inmueble == 'Casa':
            data.tipoinmueble_Casa = 1
        else:
            data.tipoinmueble_Apartamento = 1

        if tiempo_de_construido <= 1:
            data.anos_0_1 = 1
        elif tiempo_de_construido <= 10:
            data.anos_1_10 = 1
        elif tiempo_de_construido <= 30:
            data.anos_10_30 = 1
        else:
            data.anos_30 = 1

        if tipo_negocio == 'Sólo Venta':
            data.tiponegocio_Venta = 1
        elif tipo_negocio == 'Arriendo y Venta':
            data.tiponegocio_Venta_Y_Arri = 1
        else:
            data.tiponegocio_Arriendo = 1
        print(data)
        with st.spinner('Prediciendo...'):
            model = XGBoost()
            model.load_model()
            predictions = model.predict(data.to_arr())

        st.success(f'El precio por metro cuadrado es de: {predictions[0]}')
