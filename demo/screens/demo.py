import streamlit as st


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
    area = st.number_input(
        '¿Cuál es el área de tu inmueble?', step=1, format='%d')
    banos = st.number_input('¿Cuántos baños tiene?', step=1.0, format='%d')
    garajes = st.number_input(
        '¿Cuántos garajes tiene tu inmueble?', step=1.0, format='%d')
    habitaciones = st.number_input(
        '¿Cuántas habitaciones tiene?', step=1.0, format='%d')
    piso = st.number_input(
        '¿Cuántos pisos tiene tu casa?', step=1.0, format='%d')
    valoradministracion = st.number_input(
        '¿Cuánto pagas de administración? (Si no aplica deja en 0)',
        step=1.0, format='%d'
    )

    import geopy
    from geopy.geocoders import Nominatim
    from geopy.extra.rate_limiter import RateLimiter

    street = st.sidebar.text_input("Dirección", "")
    city = st.sidebar.text_input("Ciudad", "Toronto")
    country = "Colombia"

    geolocator = Nominatim(user_agent="GTA Lookup")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(street+", "+city+", "+country)

    lat = location.latitude
    lon = location.longitude
    map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    st.map(map_data, zoom=12)
    tiempo_de_construido = st.slider('¿Cuánto años tiene de construido tu inmueble?',
                                     min_value=0,
                                     max_value=30,
                                     value=0,
                                     step=1)
    tipo_negocio = st.radio('¿Qué tipo de negocio se puede haer con la inmueble?',
                            ('Sólo Venta', 'Arriendo y Venta', 'Sólo Arriendo'))
    tipo_inmueble = st.radio(
        '¿Qué tipo de inmueble es?', ('Casa', 'Apartamento'))
