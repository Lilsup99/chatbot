import pandas as pd
from numpy import nan
import re

def columnas_a_string(df, col1, col2):
    # Crear una lista de strings para cada fila
    filas = [f"*{row[col1]}*   {row[col2]} \n  " for _, row in df.iterrows()]
    filas.insert(0,'_Seleccione por numero_ :\n ')
    # Unir las filas en un solo string
    resultado = ' \n. --> '.join(filas)
    return resultado

#lista de precios
df = pd.read_excel('ROYALPACK-6-08.xlsx').rename(columns={'Unnamed: 0':'codigo','Unnamed: 1':'descripcion',
                                                          'Unnamed: 2':'base','Unnamed: 3':'precio'})
df = df.set_index('codigo', drop=False)

#etiquetado
df['label'] = nan
regex = r'\d'
# for i in df.index:
#     if re.match(regex,str(df['codigo'][i])):
#         marca = str(df['codigo'][i])
#     else:
#         df['label'][i] = marca

indices = [i for i in range(1,46)]
items = df[df['codigo'].isin(indices)]

bolsas_item = columnas_a_string(items[0:19],'codigo','descripcion')
vasos_item = columnas_a_string(items.loc[[37,38,39,40,41]],'codigo','descripcion')
papel_item = columnas_a_string(items.loc[[20,21]],'codigo','descripcion')
cajas_item = columnas_a_string(items.loc[[27,28,31]],'codigo','descripcion')
anime_item = columnas_a_string(items.loc[[24,25,26]],'codigo','descripcion')
paveca_item = columnas_a_string(items.loc[[34]],'codigo','descripcion')
pitillos_item = columnas_a_string(items.loc[[36]],'codigo','descripcion')
tina_base_item = columnas_a_string(items.loc[[29,30,33,32]],'codigo','descripcion')
utencilios_item = columnas_a_string(items.loc[[35,43,44,45]],'codigo','descripcion')

mensaje = "¡Hola! 👋\n\nBienvenido a nuestro asistente virtual. ¿En cuál de nuestros productos estás interesado? Por favor, selecciona una opción para que podamos ayudarte mejor."

intro = '\n\n *.Bolsas \n*.Vasos \n *.Papel envolver \n *.Cajas \n *.Anime \n *.Productos Paveca \n *. Otros \n *.Horarios'


mensaje = mensaje + intro

otros = ''' ¿Buscabas?: \n
        *. Pitillos \n
        *. Tinas / bases para torta \n
        *. Utencilios 
'''

FAQ = [{'user':'Hola', 'bot':mensaje},
       {'user':'Hola buen dia', 'bot':mensaje},
       {'user':'Hola buenas tardes', 'bot':mensaje},
       {'user':'Hola como esta', 'bot':mensaje},


       {'user': 'bolsas', 'bot': bolsas_item},
       {'user':'bolsa', 'bot': bolsas_item},
        {'user':'vasos','bot':vasos_item},
        {'user':'vaso', 'bot':vasos_item},
        {'user':'papel', 'bot':papel_item},
        {'user':'papel envolver', 'bot':papel_item},
        {'user':'caja', 'bot':cajas_item},
        {'user':'cajas', 'bot':cajas_item},
        {'user':'paveca', 'bot':paveca_item},
        {'user':'anime', 'bot':anime_item},
        {'user':'otro', 'bot':otros},
        {'user':'otros', 'bot':otros},
        {'user':'pitillo', 'bot':pitillos_item},
        {'user':'pitillos', 'bot':pitillos_item},
        {'user':'tina', 'bot':tina_base_item},
        {'user':'tinas', 'bot':tina_base_item},
        {'user':'base', 'bot':tina_base_item},
        {'user':'bases', 'bot':tina_base_item},
        {'user':'base torta', 'bot':tina_base_item},
        {'user':'bases torta', 'bot':tina_base_item},
        {'user':'bases tortas', 'bot':tina_base_item},
        {'user':'bases de tortas', 'bot':tina_base_item},
        {'user':'utencilios', 'bot':utencilios_item},
    #    {'user':'vasos', 'bot':tipo_vaso},
       #{'user':'', 'bot':''}


        #    {'user':'', 'bot':''},
    #    'user':'', 'bot':'',
        ]





# training_conversations = [
#     {"usuario": "Hola", "bot": "Hola! ¿En qué puedo ayudarte hoy?"},
#     {"usuario": "¿Puedes recomendarme una película?", "bot": "Claro, ¿qué tipo de películas te gustan?"},
#     {"usuario": "Me gustan las películas de acción.", "bot": "Te recomiendo 'Mad Max: Fury Road'. Es una excelente película de acción."},
#     {"usuario": "¿Y una comedia?", "bot": "Te sugiero 'Superbad'. Es muy divertida."},
#     {"usuario": "¿Qué hay de las películas de ciencia ficción?", "bot": "'Inception' es una gran película de ciencia ficción que te hará pensar."},
#     {"usuario": "¿Alguna película de terror?", "bot": "Si te gustan las películas de terror, te recomiendo 'The Conjuring'."},
#     {"usuario": "¿Qué tal una película romántica?", "bot": "'The Notebook' es una hermosa película romántica que seguramente te encantará."},
#     {"usuario": "Quiero ver una película de animación.", "bot": "Te recomiendo 'Toy Story'. Es un clásico de la animación."},
#     {"usuario": "¿Puedes recomendarme una serie?", "bot": "Por supuesto. ¿Qué género de series te gusta?"},
#     {"usuario": "Me gustan las series de drama.", "bot": "Te sugiero 'Breaking Bad'. Es una serie de drama muy aclamada."},
#     {"usuario": "¿Y una serie de comedia?", "bot": "Te recomiendo 'Friends'. Es una de las mejores series de comedia."},
#     {"usuario": "Quiero ver una serie de ciencia ficción.", "bot": "'Stranger Things' es una excelente opción de ciencia ficción."},
#     {"usuario": "¿Tienes alguna recomendación de serie de terror?", "bot": "'The Haunting of Hill House' es una serie de terror muy buena."},
#     {"usuario": "¿Qué tal una serie romántica?", "bot": "'Outlander' es una serie romántica con una gran historia."},
#     {"usuario": "¿Puedes recomendarme una película familiar?", "bot": "'The Lion King' es una maravillosa película familiar."},
#     {"usuario": "¿Y una película de aventura?", "bot": "'Indiana Jones: Raiders of the Lost Ark' es una excelente película de aventura."},
#     {"usuario": "Gracias por las recomendaciones.", "bot": "De nada! Espero que disfrutes las películas y series. ¿Hay algo más en lo que pueda ayudarte?"},
#     {"usuario": "No, eso es todo por ahora.", "bot": "¡Perfecto! Que tengas un buen día."},
#     {"usuario": "Adiós", "bot": "¡Adiós! Hasta luego."}
# ]