# Repository for challenge EL ALGORITMO ES CORRECTO

By:
- [Nestor Sebastian Garzon Contreras](https://www.linkedin.com/in/sebastiangarzonc/)
- [Santiago Leonardo Delgado Mejia](https://www.linkedin.com/in/santiago-leonardo-delgado-mej%C3%ADa-8a97811a8/)

# Descripción de la metodología: 
Se hizo un EDA para entender y limpiar más de 250 mil registros que se nos entregó. Se consideraron variables importantes: ‘area', 'banos', 'estrato', 'garajes', 'habitaciones', 'piso', 'valoradministracion','valorventa','latitud', 'longitud',’tipoinmueble’,‘tiponegocio’, ‘tiempodeconstruido’.
Para los atributos ‘area’, 'valoradministracion' y 'valorventa', ‘habitaciones’ y ‘valor_mcuadrado’, se filtraron los datos atipicos escogiendo una cota inferior y superior de percentiles.
También se hizo un análisis espacial, intersectando los puntos con las manzanas de Bogotá y contrastando la veracidad del ‘estrato’ con los datos oficiales.
Luego se codificaron las variables categóricas, para poder entrenar a tres tipos de modelos:
XGboost: para el modelo se utilizó RandomizedSearchCV el cual permite busca aleatoriamente entre un diccionario de hiperparametros dados encontrar el mejor modelo, de esta búsqueda aleatoria ese entrenaron automáticamente 50 modelos, con diferentes parámetros y se identificó al mejor de ellos tomando como valor a buscar el valor del metro cuadrado calculado con los valores que se tenían en el dataset de entrenamiento.
Kmeans: Al no tenerse los valores reales, se utilizó aprendizaje no supervisado que agrupara los datos determinando cuáles de ellos eran similares y así identificar predios similares, tanto en características como en precio. Con diferentes modelos, haciendo uso el artículo 11 de la resolución 620 del 23 de septiembre de 2008 del AGUSTÍN CODAZZI, se filtró por aquellos que tuvieran un coeficiente de variación menor al 7,5%.

# Resultados
Para el aprendizaje supervisado el mejor modelo fue XGBoost sobre redes neuronales obteniendo un accuracy del 0.9956, un MAPE de 0.020 y en Kaggle un MAPE de 5.072
Para aprendizaje no supervisado solo se usó k-means obteniendo un MAPE en Kaggle de 5.394

# Pasos a seguir

Se plantea mejorar nuestra solución usando más datos de entrenamiento y con el precio Habi para obtener una mayor precisión en el modelo.
Poner el modelo en producción, ya sea desde la plataforma de Habi o alguna otra plataforma.
Hacer una prueba con distintos grupos de usuarios e ir escalando el tamaño de estos grupos, probando la eficacia del algoritmo e iterando hasta encontrar el algoritmo más apropiado en un entorno real. (A/B Testing)

# Retos encontrados
Cuando se realizó el EDA se encontró casas en que su ubicación era sobre aeropuertos, autopistas o el estrato de las casas no eran los mismos a los de los datos oficiales,  adicionalmente se observó que las ubicaciones de los datos de test se concentraban en unos puntos muy específicos de la ciudad, lo cual no es una muestra representativa de los datos ni de la efectividad de nuestros modelos (orientado a toda la ciudad). Estos retos se observaron con la ayuda de la herramienta QGIS.

### Ubicación inconsistente
<img src='https://raw.githubusercontent.com/nestorsgarzonc/el_algoritmo_es_correcto_challenge_data_science/6eab9822a878e9f0fd47d78ce58f242f768e3ac2/ubicacion_inconsistente.png' width='500px'/>

### Cosas raras 1
<img src='https://raw.githubusercontent.com/nestorsgarzonc/el_algoritmo_es_correcto_challenge_data_science/5859af6968cd9c591e3cdf9f9ae31039c555d752/cosas_raras.png' width='500px'/>

### Cosas raras 2 geo test
<img src='https://raw.githubusercontent.com/nestorsgarzonc/el_algoritmo_es_correcto_challenge_data_science/5859af6968cd9c591e3cdf9f9ae31039c555d752/cosas_raras_geo_test.png' width='500px'/>

### Cosas raras 3
<img src='https://raw.githubusercontent.com/nestorsgarzonc/el_algoritmo_es_correcto_challenge_data_science/9fe28192c4c6f10ecbcba2d743aad2ab9a7469c8/cosas_raras_3.png' width='500px'/>

### Cosas raras 4
<img src='https://raw.githubusercontent.com/nestorsgarzonc/el_algoritmo_es_correcto_challenge_data_science/9fe28192c4c6f10ecbcba2d743aad2ab9a7469c8/cosas_raras_4.png' width='500px'/>





# [Link de Github](https://github.com/nestorsgarzonc/el_algoritmo_es_correcto_challenge_data_science)


