

# Machine Learning Operations (MLOps)
## Proyecto Individual # 1 | Sistema de Recomendación de Películas
## Introducción:
El presente proyecto práctico forma parte del curriculum para la carrera de Ciencia de Datos impartido por **Henry** como parte del trayecto de Labs. El mismo consiste en la elaboración de un Sistema de Recomendación de películas cumpliendo cuatro (04) etapas principales
1. Trabajo de ETL **(Extract, Transform, Load)** en un conjunto de datasets (proporcionados por la institución).
2. Trabajo de EDA  **(Exploratory Data Analysis)** a los datos resultantes del procedimiento enunciado en el punto 1
3. Trabajo de ML **(machine learning)** para armar un sistema de recomendación de películas.
4. Trabajo de crear y realizar deploy de API **(Application Programming Interface)** donde quede a disposición la información necesaria para su consumo respetando y cumpliendo las características y requerimientos solicitados en el programa
## 1. El set de datos

La información recolectada se encuentra en dos (02) archivo CSV (`movies_dataset.csv` y `credits.csv`) los cuales lo encontraras en el enlace con las siguientes características:<br>

[Archivos `movies_dataset.csv` y `credits.csv`](https://drive.google.com/drive/folders/1hsmKrY2O-nlOF4_BJuEd7ti3MCrF_6Cz?usp=sharing)<br>
la carpeta datasets deberá colocarse en el directorio raíz del oproyecto para que funcionen los path predeterminados en el proyecto

* **`movies_dataset`**: 45466 filas y 24 columnas.
* **`credits`** : 45476 filas y 3 columnas.

 Las columnas para **`movies_dataset`** son:<br>
 

|Característica | Descripción|
|:-------------:|:---------- |
| adult |	Indica si la película tiene califiación X, exclusiva para adultos.|
| belongs_to_collection | Un diccionario que indica a que franquicia o serie de películas pertenece la película|
| budget |	El presupuesto de la película, en dólares |
| genres |	Un diccionario que indica todos los géneros asociados a la película|
| homepage | La página web oficial de la película|
| id | ID de la pelicula|
| imdb_id |IMDB ID de la pelicula|
| original_language | Idioma original en la que se grabo la pelicula |
| original_title | Titulo original de la pelicula |
| overview | Pequeño resumen de la película|
| popularity | Puntaje de popularidad de la película, asignado por TMDB (TheMoviesDataBase) |
| poster_path |	URL del póster de la película |
| production_companies | Lista con las compañias productoras asociadas a la película |
| production_countries | Lista con los países donde se produjo la película |
| release_date | Fecha de estreno de la película |
| revenue |	Recaudación de la pelicula, en dolares |
| runtime |	Duración de la película, en minutos |
| spoken_languages | Lista con los idiomas que se hablan en la pelicula |
| status | Estado de la pelicula actual (si fue anunciada, si ya se estreno, etc) |
| tagline |	Frase celebre asociada a la pelicula |
| title | Titulo de la pelicula |
| video | Indica si hay o no un trailer en video disponible en TMDB |
| vote_average | Puntaje promedio de reseñas de la pelicula |
| vote_count | Numeros de votos recibidos por la pelicula, en TMDB |


