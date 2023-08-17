import spacy
import string
from spacy.lang.pt.stop_words import STOP_WORDS
import en_core_web_sm
import re
import customtkinter as ctk
from tkinter import *

pln = en_core_web_sm.load()
stop_words = STOP_WORDS


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


def margim(largura):
    margem = ctk.CTkCanvas(highlightthickness=0, height=largura, background='#242424')
    margem.pack()


def classifica():
    modelo = spacy.load('modelo')

    frase = text.get()
    frase = preprocessamento(frase)

    previsao = modelo(frase).cats
    if previsao['POSITIVO'] > previsao['NEGATIVO']:
        result.configure(text='A frase foi classificada Positiva!')
    else:
        result.configure(text='A frase foi classificada Negativa!')


root = ctk.CTk()
root.title('Classificador de Frase')
root.geometry('500x300')
root.minsize(500, 300)
root.maxsize(500, 300)

margim(40)
title = ctk.CTkLabel(root, text='Classificador de frase Positivo ou Negativo', font=('Montserrat', 20, 'bold'),
                     text_color='#FFF')
title.pack()

margim(15)
text = ctk.CTkEntry(root, placeholder_text='Digite a frase para ser classificada', fg_color='transparent',
                    placeholder_text_color='#FFF', width=300, font=('Montserrat', 13, 'bold'), justify=CENTER)
text.pack()

margim(15)
button = ctk.CTkButton(root, text='Classificar', font=('Montserrat', 18, 'bold'), text_color='#FFF', command=classifica)
button.pack()

margim(20)
result = ctk.CTkLabel(root, text='', font=('Montserrat', 20, 'bold'), text_color='#FFF')
result.pack()
root.mainloop()



