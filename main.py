#!venv/bin/python

# Estamos fazendo o http://www.kaggle.com/c/titanic
# O teste mais simples de todos para entender o fluxo do programa e chutar todos os resultados com 0

import pandas as pd

# carregar um dataframe do pandas a partir do arquivo test.csv obtido do kaggle
dataframe = pd.read_csv('test.csv')


# Gerar o resultado (todos morreram)
def chutarquetodomundomorreu(x):
    # cria um novo dataframe Y com apenas a coluna PassengerId da coluna x
    y = x[['PassengerId']]
    # adiciona uma nova coluna ao novo dataframe Y, inicializando todos os valores com 0
    y['Survived'] = 0

    return y


# gera o resultado a partir da nossa func
resultado = chutarquetodomundomorreu(dataframe)

#
resultado.to_csv('chute1.csv', index=False)
