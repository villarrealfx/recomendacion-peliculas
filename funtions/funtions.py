# Importar modulos necesarios
import pandas as pd
import numpy as np
import pickle
from ast import literal_eval

class Movies:
    def __init__(self, path, path_r) -> None:
        self.df = pd.read_csv(path)
        self.df_r = pd.read_csv(path_r)
        self.df_r.recommendation = self.df_r.recommendation.apply(literal_eval)
        self.shape = self.df.shape
        self.columns = self.df.columns.values
        self.df_coun = self.df[['production_countries']]


    def get_lang(self, idioma:str):
        '''
        Función para obtener el codigo iso639 de un pais o el nombre del mismo escrito en el idioma original
        '''
        lang = {
                'aa' : 'afar',
                'ab' : 'abjasio',  # (o abjasiano)
                'ae' : 'avéstico',
                'af' : 'afrikáans',
                'ak' : 'akano',
                'am' : 'amhárico',
                'an' : 'aragonés',
                'ar' : 'العربية',
                'as' : 'asamés',
                'av' : 'avar',  # (o ávaro)
                'ay' : 'aimara',
                'az' : 'azerí',
                'ba' : 'baskir',
                'be' : 'беларуская мова',
                'bg' : 'български език',
                'bh' : 'bhoyapurí',
                'bi' : 'bislama',
                'bm' : 'bamanankan',
                'bn' : 'বাংলা',
                'bo' : 'tibetano',
                'br' : 'bretón',
                'bs' : 'bosanski',
                'ca' : 'català',
                'ce' : 'checheno',
                'ch' : 'chamorro',
                'co' : 'corso',
                'cr' : 'cree',
                'cs' : 'český',
                'cu' : 'eslavo',  # eclesiástico antiguo
                'cv' : 'chuvasio',
                'cy' : 'cymraeg',
                'da' : 'dansk',
                'de' : 'deutsch',
                'dv' : 'maldivo',  # (o dhivehi)
                'dz' : 'dzongkha',
                'ee' : 'ewé',
                'el' : 'ελληνικά',  # (moderno)
                'en' : 'english',
                'eo' : 'esperanto',
                'es' : 'español',  # (o castellano)
                'et' : 'eesti',
                'eu' : 'euskera',
                'fa' : 'فارسی',
                'ff' : 'fula',
                'fi' : 'suomi',  # (o finlandés)
                'fj' : 'fiyiano',  # (o fiyi)
                'fo' : 'feroés',
                'fr' : 'français',
                'fy' : 'frisón',  # (o frisio)
                'ga' : 'gaeilge',  # (o gaélico)
                'gd' : 'gaélico',  # escocés
                'gl' : 'galego',
                'gn' : 'guaraní',
                'gu' : 'guyaratí',  # (o gujaratí)
                'gv' : 'manés',  # (gaélico manés o de Isla de Man)
                'ha' : 'hausa',
                'he' : 'עִבְרִית',
                'hi' : 'हिन्दी',  # (o hindú)
                'ho' : 'hiri',  # motu
                'hr' : 'hrvatski',
                'ht' : 'haitiano',
                'hu' : 'magyar',
                'hy' : 'armenio',
                'hz' : 'herero',
                'ia' : 'interlingua',
                'id' : 'bahasa indonesia',
                'ie' : 'occidental',
                'ig' : 'igbo',
                'ii' : 'yi de Sichuán',
                'ik' : 'iñupiaq',
                'io' : 'ido',
                'is' : 'íslenska',
                'it' : 'italiano',
                'iu' : 'inuktitut',  # (o inuit)
                'ja' : '日本語',
                'jv' : 'javanés',
                'ka' : 'ქართული',
                'kg' : 'kongo',  # (o kikongo)
                'ki' : 'kikuyu',
                'kj' : 'kuanyama',
                'kk' : 'қазақ',  # (o kazajio)
                'kl' : 'groenlandés',  # (o kalaallisut)
                'km' : 'camboyano',  # o jemer)
                'kn' : 'Kannada',
                'ko' : '한국어/조선말',
                'kr' : 'kanuri',
                'ks' : 'cachemiro',  # (o cachemir)
                'ku' : 'kurdo',
                'kv' : 'komi',
                'kw' : 'córnico',
                'ky' : 'kirghiz',
                'la' : 'latín',
                'lb' : 'luxemburgués',
                'lg' : 'luganda',
                'li' : 'limburgués',
                'ln' : 'lingala',
                'lo' : 'lao',
                'lt' : 'lietuvi\x9akai',
                'lu' : 'luba-katanga',  # (o chiluba)
                'lv' : 'latviešu',
                'mg' : 'malgache',  # (o malagasy)
                'mh' : 'marshalés',
                'mi' : 'maorí',
                'mk' : 'macedonio',
                'ml' : 'malayalam',
                'mn' : 'mongol',
                'mr' : 'maratí',
                'ms' : 'bahasa melayu',
                'mt' : 'malti',
                'my' : 'birmano',
                'na' : 'nauruano',
                'nb' : 'bokmål',  # bokmål
                'nd' : 'ndebele del norte',
                'ne' : 'nepalí',
                'ng' : 'ndonga',
                'nl' : 'nederlands',  # (u holandés)
                'nn' : 'nynorsk',
                'no' : 'norsk',
                'nr' : 'ndebele del sur',
                'nv' : 'navajo',
                'ny' : 'chichewa',
                'oc' : 'occitano',
                'oj' : 'ojibwa',
                'om' : 'oromo',
                'or' : 'oriya',
                'os' : 'osético',  # (u osetio, u oseta)
                'pa' : 'ਪੰਜਾਬੀ', # (o penyabi)
                'pi' : 'pali',
                'pl' : 'polski',
                'ps' : 'پښتو',  # (o pastún, o pashto)
                'pt' : 'português',
                'qc' : 'quechua',
                'rm' : 'romanche',
                'rn' : 'kirundi',
                'ro' : 'română',
                'ru' : 'pусский',
                'rw' : 'kinyarwanda',  # (o kiñaruanda)
                'sa' : 'sánscrito',
                'sc' : 'sardo',
                'sd' : 'sindhi',
                'se' : 'sami septentrional',
                'sg' : 'sango',
                'si' : 'cingalés',
                'sk' : 'slovenčina',
                'sl' : 'slovenščina',
                'sm' : 'samoano',
                'sn' : 'shona',
                'so' : 'somalí',
                'sq' : 'shqip',
                'sr' : 'srpski',
                'ss' : 'suazi',  # (o swati, o siSwati)
                'st' : 'sesotho',
                'su' : 'sundanés',  # (o sondanés)
                'sv' : 'svenska',
                'sw' : 'kiswahili',
                'ta' : 'தமிழ்',
                'te' : 'తెలుగు',
                'tg' : 'tayiko',
                'th' : 'ภาษาไทย',
                'ti' : 'tigriña',
                'tk' : 'turcomano',
                'tl' : 'tagalo',
                'tn' : 'setsuana',
                'to' : 'tongano',
                'tr' : 'türkçe',
                'ts' : 'tsonga',
                'tt' : 'tártaro',
                'tw' : 'twi',
                'ty' : 'tahitiano',
                'ug' : 'uigur',
                'uk' : 'український',
                'ur' : 'اردو',
                'uz' : 'ozbek',
                've' : 'venda',
                'vi' : 'tiếng việt',
                'vo' : 'volapük',
                'wa' : 'valón',
                'wo' : 'wolof',
                'xh' : 'xhosa',
                'yi' : 'yídish',  # (o yidis, o yiddish)
                'yo' : 'yoruba',
                'za' : 'chuan',  # (o chuang, o zhuang)
                'zh' : '普通话',
                'zu' : 'isizulu',
                'cn' : '广州话/廣州話',
                'Sin Idioma': 'no language'
                }
        
        if len(idioma)>2:
            for k, v in lang.items():
                if v == idioma.lower():
                    return k, v
        else:
            for k, v in lang.items():

                if k == idioma.lower():
                    return k, v
        return False        

    def peliculas_idioma(self, idioma):
         '''
         Retornar la cantidad de películas en un idioma pasado como parámetro.

         Parametros
         ----------

         idioma: str el nombre de un idioma o el código iso 639
         '''
         return self.df.loc[self.df['original_language'] == idioma].shape[0]
           
    def peliculas_duracion(self, pelicula):

        '''
         Retornar la duración en minutos y el año de extreno de la película pasada como parámetro.

         Parametros
         ----------

         pelicula: str el nombre de una película
        '''

        resul = self.df[self.df['title'] == pelicula]

        if len(resul) == 0:
            return False
        else:
            movie_length = resul['runtime'].values[0]
            year = resul['release_year'].values[0]
            print(year, movie_length)
            return movie_length, year

    def franquicia(self, franquicia):
        
        '''
         Retornar la cantidad de peliculas, ganancia total y ganancia promedio de la franquicia pasada como parámetro.

         Por criterio del problema se tomará como ganancia la columna "revenue" 

         Parametros
         ----------

         franquicia: str el nombre de la franquisia
        '''

        resul = self.df.loc[self.df['belongs_to_collection'] == franquicia]
        if len(resul) == 0:
            return False
        else:
            amount_movies = resul.shape[0]
            total_revenue = round(resul.revenue.sum()/1000000, 2)
            mean_revenue = round(resul.revenue.mean()/1000000, 2)
            return amount_movies, total_revenue, mean_revenue


    def peliculas_pais(self, pais):
                    
        '''
        Retornar la cantidad de peliculas producidas en el país pasado como parámetro.

        Parametros
        ----------

        pais: str el nombre del país según se encuentra en la base de datos
        '''
        
        df_coun = self.df.loc[:,['title','production_countries']]
        df_coun['production_countries'] = df_coun['production_countries'].apply(eval)
        df_coun = df_coun.explode('production_countries')
        resul = df_coun[df_coun['production_countries'] == pais].shape[0]
        
        return resul


    def productoras_exitosas(self, productora):
        '''
        Retorna el revunue total y la cantidad de peliculas que realizo la productora pasada por parámetro 


        Parametros
        ----------

        productora: str el nombre de la productora según se encuentra en la base de datos
        '''

        df_produc = self.df.loc[:,['production_companies','revenue']]
        df_produc['production_companies'] = df_produc['production_companies'].apply(eval)
        df_produc = df_produc.explode('production_companies')

        total_revenue = round(df_produc[df_produc['production_companies'] == productora]['revenue'].sum()/1000000, 2)
        amount_movies = df_produc[df_produc['production_companies'] == productora].shape[0]

        return total_revenue, amount_movies
    

    def director(self, nombre_director):
        '''
        retorna el éxito medido a través del retorno del director pasado por parámetro. 
        
        La función retornará ademas del exito del director lo siguiente en una lista:
        nombre de cada película, fecha de lanzamiento, retorno individual, costo y ganancia de la misma. 
        '''

        df_director = self.df.loc[:,['director', 'title', 'release_date','return', 'budget','revenue']]

        if len(df_director[df_director['director'] == nombre_director]) == 0:
            return False
        else:
            budget_director = df_director[df_director['director'] == nombre_director]['budget'].sum()
            revenue_director = df_director[df_director['director'] == nombre_director]['revenue'].sum()
            return_direct = round(revenue_director/budget_director, 2)

            movies_director = df_director[df_director['director'] == nombre_director].values
            records_director = []

            for l in range(len(movies_director)):
                dict_director = {
                    'title': movies_director[l][1],
                    'release_date': movies_director[l][2],
                    'return': round(movies_director[l][3], 2),
                    'budget_MM$': round(movies_director[l][4]/1000000, 2),
                    'revenue_MM$': round(movies_director[l][5]/1000000, 2)    
                    }
                records_director.append(dict_director)

            return return_direct, records_director
        

    def recomendacion(self, title, cosine_sim, df, indices):
        '''
        Retornar las 5 películas mas similares a la película pasada como parámetro.
        
        La función presenta una lógica estructuradacomo sigue:
            1. Se Obtiene el índice de la película que coincide con el título.
            2. Se Obtiene los puntajes de similitud por pares de todas las películas con esa película y
            la convierte en una lista de tuplas.
            3. Se Ordenan las películas según las puntuaciones de similitud del coseno.
            4. Se Obtienen los puntajes de las 5 películas más similares. Ignorando la primera película.
            5. Se Obtienen los índices de películas.
            6. Se Retorna las 5 películas más similares.
            
        Parametros:
        ----------
        title: str = Obligatorio titulo de la película 
        cosine_sim: ndarray = Puntuación de similitud del coseno
        df: pandas.core.frame.DataFrame = Fuente de datos
        indices: pandas.core.series.Series = index
        '''

        try:

            idx = indices[title]

            sim_scores = list(enumerate(cosine_sim[idx]))

            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            sim_scores = sim_scores[1:6]

            movie_indices = [i[0] for i in sim_scores]

            return df['title'].iloc[movie_indices].values.tolist()
        except:
            return False
        
        
    def ml_recomm(self, titulo):

        '''
        Retornar las 5 películas mas similares a la película pasada como parámetro.
        
        La función presenta una lógica estructuradacomo sigue:
            1. Se Obtiene el índice de la película que coincide con el título.
            2. Se Obtiene los puntajes de similitud por pares de todas las películas con esa película y
            la convierte en una lista de tuplas.
            3. Se Ordenan las películas según las puntuaciones de similitud del coseno.
            4. Se Obtienen los puntajes de las 5 películas más similares. Ignorando la primera película.
            5. Se Obtienen los índices de películas.
            6. Se Retorna las 5 películas más similares.
            
        Parametros:
        ----------
        title: str = Obligatorio titulo de la película 
        cosine_sim: ndarray = Puntuación de similitud del coseno
        df: pandas.core.frame.DataFrame = Fuente de datos
        indices: pandas.core.series.Series = index
        '''

        resul = self.df_r[self.df_r['movie'] == titulo]
        if len(resul) == 0:
            return False

        else:
            return resul['recommendation'].values[0]