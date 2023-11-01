# Classificador de Frases Positivas ou Negativas

Este é um aplicativo simples de classificação de frases desenvolvido em Python usando a biblioteca Spacy para processamento de linguagem natural (PNL). O aplicativo utiliza um modelo pré-treinado para classificar frases como positivas ou negativas.

## Funcionalidades

- **Classificação de Frases:** Permite aos usuários digitar uma frase para ser classificada como positiva ou negativa.

## Requisitos

- Python 3.x
- Biblioteca Spacy

## Como Executar

1. Certifique-se de ter o Python instalado. <br>Você pode baixá-lo em [python.org](https://www.python.org/).

2. Instale a biblioteca Spacy usando o seguinte comando:<br>
pip install -U spacy

3. Baixe e instale o modelo pré-treinado do Spacy para o processamento de língua portuguesa:<br>
python -m spacy download pt_core_news_sm

4. Clone este repositório:<br>
git clone https://github.com/Samuel-Gaudencio/classificador_sentimentos.git

5. Navegue até o diretório do projeto:<br>
cd classificador-de-frases

6. Execute o aplicativo:<br>
python main.py

## Customização

- O modelo utilizado para a classificação de frases está localizado no arquivo `modelo`. Você pode treinar um novo modelo ou substituir o modelo existente conforme necessário.

- O aplicativo utiliza uma interface gráfica desenvolvida com a biblioteca `customtkinter`. Você pode personalizar a aparência da interface gráfica editando o código em `main.py`.
