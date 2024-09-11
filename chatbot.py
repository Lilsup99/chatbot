###
import collections.abc

collections.Hashable = collections.abc.Hashable
###


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import faq
import pandas as pd
from numpy import nan
import re



def columnas_a_string(df, col1, col2):
    # Crear una lista de strings para cada fila
    filas = [f"{row[col1]:<10}  *{row[col2]}*"+'$' for _, row in df.iterrows()]
    # Unir las filas en un solo string
    resultado = '\n \n'.join(filas)
    resultado = resultado + '\n\n *ESTOS PRECIOS INCLUYEN IVA* \n\n *Para hacer compra comunicarse al*: +584121497412'
    return resultado

#lista de precios
df = pd.read_excel('ROYALPACK-6-08.xlsx').rename(columns={'Unnamed: 0':'codigo','Unnamed: 1':'descripcion',
                                                          'Unnamed: 2':'base','Unnamed: 3':'precio'})
df = df.set_index('codigo', drop=False)

#etiquetado
df['label'] = nan
marca = 1
regex = r'\d'
for i in df.index:
    if re.match(regex,str(df['codigo'][i])):
        marca = str(df['codigo'][i])
    else:
        df['label'][i] = marca



#'chatterbot.logic.MathematicalEvaluation',
bot = ChatBot(
    'Karim2',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    logic_adapters=['chatterbot.logic.BestMatch']
    #storage_adapter='chatterbot.storage.SQLStorageAdapter',
    #database_uri='sqlite:///database.sqlite3'
)
bot.storage.drop()
trainer = ListTrainer(bot)
training_data = [[conversation["user"], conversation["bot"]] for conversation in faq.FAQ]

for data in training_data:
    trainer.train(data)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.spanish')


def respuesta(msj):
    if msj in [str(i) for i in range(1,46)]:
        temp = df[df['label']==msj]
        return columnas_a_string(temp,'descripcion','precio')
    else:
        return bot.get_response(msj)

# print(faq.intro)
# while True:
#     try:
#         promt = input('ask: ')
#         bot_input = bot.get_response(promt)
#         if promt in [str(i) for i in range(1,46)]:
#             temp = df[df['label']==promt]
#             print(columnas_a_string(temp,'descripcion','precio'))
#         else:
#             print(bot_input)

#     except(KeyboardInterrupt, EOFError, SystemExit):
#         break
