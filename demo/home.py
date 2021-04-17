import plotly.figure_factory as ff
import plotly.express as px
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def filter_by_quantile(df: pd.DataFrame, name_col: str, min=0, max=0.9999):
    min_val = df[name_col].quantile(min)
    max_val = df[name_col].quantile(max)
    return df[(df[name_col] >= min_val) & (df[name_col] <= max_val)]


def home():
    df = pd.read_csv('../data/test_data.csv')
    st.title('Equipo N&L')
    st.text('By:')
    st.text('Nestor Sebastian Garzon Contreras')
    st.text('Santiago Leonardo Delgado Mejia')
    st.markdown('# Descripción de la metodología:')
    st.markdown('Se hizo un EDA para entender y limpiar más de 250 mil registros que se nos entregó. Se consideraron variables importantes: ')
    st.code("""
    ‘area', 'banos', 'estrato', 'garajes', 'habitaciones', 'piso', 
    'valoradministracion','valorventa','latitud', 'longitud', 
    ’tipoinmueble’, ‘tiponegocio’, ‘tiempodeconstruido’
    """)
    # col1, col2 = fig2ig1)
    # st.pyplot_chart(fig1)
    # # fig1 = ff.create_distplot(hist_data)
    # col1.plotly_chart(fig1, use_container_width=True)

    # col2.header('Valorventa')
    hist_data2 = filter_by_quantile(df, 'valorventa', min=0.001, max=0.99)
    # fig2 = px.histogram(hist_data2, x='valorventa', nbins=range(0, 1e15, 1e14))
    fig2 = plt.figure()
    fig2.hist(hist_data2['valorventa'])
    # fig2 = ff.create_distpolot(hist_data2)
    # col2.plotly_chart(fig2, use_container_width=True)

    st.plotly_chart(fig2)

    descriptionMethodology = """
    se filtraron los datos atipicos escogiendo una cota inferior y superior de percentiles.
    También se hizo un análisis espacial, intersectando los puntos con las manzanas de Bogotá y contrastando la veracidad del ‘estrato’ con los datos oficiales.
    Luego se codificaron las variables categóricas, para poder entrenar a tres tipos de modelos:
    - XGboost: para el modelo se utilizó RandomizedSearchCV el cual permite busca aleatoriamente entre un diccionario de hiperparametros dados encontrar el mejor modelo, de esta búsqueda aleatoria ese entrenaron automáticamente 50 modelos, con diferentes parámetros y se identificó al mejor de ellos tomando como valor a buscar el valor del metro cuadrado calculado con los valores que se tenían en el dataset de entrenamiento.
    - Kmeans: Al no tenerse los valores reales, se utilizó aprendizaje no supervisado que agrupara los datos determinando cuáles de ellos eran similares y así identificar predios similares, tanto en características como en precio. Con diferentes modelos, haciendo uso el artículo 11 de la resolución 620 del 23 de septiembre de 2008 del AGUSTÍN CODAZZI, se filtró por aquellos que tuvieran un coeficiente de variación menor al 7,5%.
    """
    st.markdown(descriptionMethodology)

    resultados = """
        # Resultados
    Para el aprendizaje supervisado el mejor modelo fue XGBoost sobre redes neuronales obteniendo un accuracy del 0.9956, un MAPE de 0.020 y en Kaggle un MAPE de 5.072
    Para aprendizaje no supervisado solo se usó k-means obteniendo un MAPE en Kaggle de 5.394
    """
    st.markdown(resultados)

    pasos_a_seguir = """
    # Pasos a seguir

    - Se plantea mejorar nuestra solución usando más datos de entrenamiento y con el precio Habi para obtener una mayor precisión en el modelo.
    - Poner el modelo en producción, ya sea desde la plataforma de Habi o alguna otra plataforma.
    - Hacer una prueba con distintos grupos de usuarios e ir escalando el tamaño de estos grupos, probando la eficacia del algoritmo e iterando hasta encontrar el algoritmo más apropiado en un entorno real. (A/B Testing)
    """
    st.markdown(pasos_a_seguir)

    retos_encontrados = """
    # Retos encontrados
    Cuando se realizó el EDA se encontró casas en que su ubicación era sobre aeropuertos, autopistas o el estrato de las casas no eran los mismos a los de los datos oficiales,  adicionalmente se observó que las ubicaciones de los datos de test se concentraban en unos puntos muy específicos de la ciudad, lo cual no es una muestra representativa de los datos ni de la efectividad de nuestros modelos (orientado a toda la ciudad). Estos retos se observaron con la ayuda de la herramienta QGIS.
    """
    st.markdown(retos_encontrados)

    st.markdown("### Ubicación incosistente")
    st.image('../cosas_raras_3.png')
    st.markdown("### Cosas raras")
    st.image('../cosas_raras.png')
    st.image('../cosas_raras_4.png')
    st.markdown("### Tests")
    st.image('../cosas_raras_geo_test.png')
    st.markdown("### Cosas raras 3")
    st.image('../cosas_raras_3.png')
    # st.markdown("###Cosas raras 4")

    df['lat'] = df['latitud']
    df['lon'] = df['longitud']
    st.dataframe(df)

    my_map = pd.read_csv('../data/train_data.csv')

    my_map['lat'] = my_map['latitud']
    my_map['lon'] = my_map['longitud']
    my_map = my_map.dropna(subset=['lat', 'lon'])

    col1, col2 = st.beta_columns(2)
    col1.header("Train")
    col1.map(my_map, zoom=12)
    col2.header("Test")
    col2.map(df, zoom=12)
