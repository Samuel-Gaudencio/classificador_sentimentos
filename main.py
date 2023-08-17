import pandas as pd
import string
import spacy
import en_core_web_sm
import random
import numpy as np
import re
import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
from spacy.training import Example

base_train = pd.read_csv('Train50.csv', delimiter=';')

base_train.drop(['id', 'tweet_date', 'query_used'], axis= 1, inplace=True)
# print(base_train.head())

pln = en_core_web_sm.load()
# print(pln)

stop_words = STOP_WORDS
# print(len(stop_words))


def preprocessamento(texto):
    texto = texto.lower()

    texto = re.sub(r"@[A-Za-z0-9$-_@.&+]+", ' ', texto)

    texto = re.sub(r"https?://[A-Za-z0-9./]+", ' ', texto)

    texto = re.sub(r" +", ' ', texto)

    lista_emoticon = {':)': 'emocaopositiva',
                      ':d': 'emocaopositica',
                      ':(': 'emocaonegativa'}

    for emocao in lista_emoticon:
        texto = texto.replace(emocao, lista_emoticon[emocao])

    documento = pln(texto)

    lista = []
    for token in documento:
        lista.append(token.lemma_)

    lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in string.punctuation]
    lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])

    return lista


base_train['tweet_text'] = base_train['tweet_text'].apply(preprocessamento)

base_train_final = []

for texto, emocao in zip(base_train['tweet_text'], base_train['sentiment']):
    if emocao == 1:
        dic = {'POSITIVO': True, 'NEGATIVO': False}
    elif emocao == 0:
        dic = {'POSITIVO': False, 'NEGATIVO': True}

    base_train_final.append([texto, dic.copy()])

modelo = spacy.blank('pt')
categorias = modelo.add_pipe("textcat")
categorias.add_label("POSITIVO")
categorias.add_label("NEGATIVO")
historico = []

modelo.begin_training()
for epoca in range(5):
    random.shuffle(base_train_final)
    losses = {}
    for batch in spacy.util.minibatch(base_train_final, 512):
        textos = [modelo(texto) for texto, entities in batch]
        annotations = [{'cats': entities} for texto, entities in batch]
        examples = [Example.from_dict(doc, annotation) for doc, annotation in zip(
            textos, annotations
        )]
        modelo.update(examples, losses=losses)
        historico.append(losses)

    if epoca % 5 == 0:
        print(losses)


modelo.to_disk('modelo')
