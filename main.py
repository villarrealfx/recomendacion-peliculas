from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn

from funtions.funtions import Movies

path = 'datasets/movies_reduced.csv'
path_r = 'datasets/ml_recomend.csv'

# Crear instancia de clase películas
movie = Movies(path=path, path_r=path_r)
app = FastAPI()

# En esta área se cargarian los archivos .plk los mismos no se implementaron por dificultad de recursos
# # Cargar el archivo movie_list.pkl
# with open('datasets/movie_list.pkl', 'rb') as f:
#     movie_list = pickle.load(f)

# # Cargar el archivo similarity.pkl
# with open('datasets/similarity.pkl', 'rb') as f:
#     similarity = pickle.load(f)

# # Cargar el archivo indices.pkl
# with open('datasets/indices.pkl', 'rb') as f:
#     indices = pickle.load(f)

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')

@app.get("/")
def root():
    return {"message": "Sistema de Recomendación de Películas",
            "Alumno":"Carlos Villarreal",
            "Cohorte":'PT-02'}


@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma:str):
    '''
    Retornar la cantidad de peliculas producidas en el idioma pasado por parámetro

    idioma: (str) El idioma debe ser un string y puede tomar una de las siguientes formas:
    1.- Dos (02) letras que representan el código ISO-639 del idioma por ejemplo:
            es para Español
            en para Ingles
            zh para Chino Mandarin
            ur para Urdu
    2.-  El nombre del Idioma en el propio lenguage por ejemplo:
            'العربية' para árabe
            'беларуская мова' para bielorruso
            '日本語' para japones
            'pусский' para ruso

    El idioma pasado por parámetro debe estar en los registros de la base de datos.
    '''
    idioma = idioma.strip().lower()
    language = movie.get_lang(idioma)
    if language == False:
        return JSONResponse(
                            status_code=400,
                            content={"message": "El Idioma ingresado no es válido."},
                         )
    
    resul = movie.peliculas_idioma(language[0])
    if  resul > 0:
        return {'Idioma':f'{language[0]} - {language[1]}', 'cantidad':resul} 
    else:
        return JSONResponse(
                            status_code=400,
                            content={ "message" : f"Ocurrio una excepción, no existen películas registradas en {idioma}."})


@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    '''
    retornar la duracion y el año de estreno de la pelicula pasada por parámetro

    La película pasada por parámetro debe estar en los registros de la base de datos.
    '''

    pelicula = pelicula.strip()
    print(pelicula)
    resul = movie.peliculas_duracion(pelicula=pelicula)
    print(resul)

    if  resul == False:
        return JSONResponse(status_code=400,
                            content={'message': f"Ocurrio una excepción, La película {pelicula} no se encuentra registradas en la BBDD ."})
    else:
        return {'Película':pelicula, 'Duración': resul[0], 'Año de Estreno':resul[1]}


@app.get('/franquicia/{franquicia}')
async def franquicia(franquicia:str):
    '''
    Retornar la cantidad de peliculas, ganancia total y promedio de la franquicia pasada por parámetros
    
    La Franquicia pasada por parámetro debe estar en los registros de la base de datos.
    '''
    franquicia = franquicia.strip().lower()
    resul = movie.franquicia(franquicia)
    if  resul == False:
        return JSONResponse(status_code=400,
                            content={'message': f"Ocurrio una excepción, La franquicia {franquicia} no se encuentra registradas en la BBDD ."})
    else:
        return {'franquicia':franquicia, 'cantidad':resul[0], 'ganancia_total_MM$':resul[1], 'ganancia_promedio_MM$':resul[2]}
    

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    '''
    Retornar la cantidad de peliculas producidas en el pais pasado como parámetro
    
    El pais pasado por parámetro debe estar en los registros de la base de datos.
    '''
    pais = pais.strip().lower()
    resul = movie.peliculas_pais(pais)

    return {'pais':pais, 'cantidad':resul}


@app.get('/productoras_exitosas/{productora}')
async def productoras_exitosas(productora:str):
    '''
    Ingresas la productora, entregandote el revunue total y la cantidad de películas que realizó 
    
    La Productora pasada por parámetro debe estar en los registros de la base de datos.
    '''

    productora = productora.strip().lower()

    resul = movie.productoras_exitosas(productora)

    return {'productora':productora, 'revenue_total_MM$': resul[0],'cantidad':resul[1]}


@app.get('/director/{nombre_director}')
def director(nombre_director:str):
    '''
    retorna el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. En formato lista

    El nombre pasado por parámetro debe estar en los registros de la base de datos.
    '''
    nombre_director.strip().lower()

    resul = movie.director(nombre_director)
    
    if  resul == False:
        return JSONResponse(status_code=400,
                            content={'message': f"Ocurrio una excepción, El Director {nombre_director} no se encuentra registradas en la BBDD ."})
    else:
        return {'director':nombre_director, 'retorno_total_director': resul[0], 'movies': resul[1]}
    

@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''
    Ingresas un nombre de pelicula y te recomienda las cinco (05) películas similares en una lista.

    El sistema de recomendación fue realizado con fines educativos, y para el mismo se estan utilizando
    servicios gratiutos de hosting con capacidades de RAM y CPU limitadas por tal motivo se realizó una
    reducción de la data desde 45000 registros a unos 18000 para el desarrollo de el algoritmo.
    '''

    titulo.strip().lower()

    resul = movie.ml_recomm(titulo)

    # Aqui se cargarian los archivo .pkl para la solicitud de recomendación
    # resul = movie.recomendacion(titulo, similarity, movie_list, indices) 

    if  resul == False:
        return JSONResponse(status_code=400,
                            content={'message': f"Ocurrio una excepción, La película {titulo} no se encuentra registradas en la BBDD ."})
    else:
        return {'lista recomendada': resul}