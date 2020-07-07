###############################################
###                                         ###  
### ANALISIS DE VARIANZA Y REGRESION LINEAL ###
###                                         ###
###   Integrantes:                          ###
###   Anyeli Villareal CI: 26.002.905       ###
###   Jose Luis Pacheco C.I:26.169.922      ### 
###   Dany Karam C.I: 25.147.670            ###
###   Marielba Maldonado C.I: 26.088.718    ###
###                                         ###
###############################################

from sklearn.linear_model import LinearRegression, Ridge, Lasso, BayesianRidge, TweedieRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from math import sqrt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

### Este archivo contiene el código usado para la sección 9 del trabajo.

def read_doc(path):  # El parametro es la ruta donde se encuentra almacenado el documento, seguido del nombre del mismo
    """ Lee el documento .csv de entramiento """
    document = pd.read_csv(path, error_bad_lines=False)
    document.head()

    columns = ['age', 'sex', 'bmi', 'children', 'smoker',
               'region', 'charges', 'ne', 'nw', 'se', 'sw']
    document = document[columns]
    document = document[pd.notnull(document['charges'])]
    document.columns = ['age', 'sex', 'bmi',
                        'children', 'smoker', 'region', 'charges', 'ne', 'nw', 'se', 'sw']

    return document


def train_model(document, drop):  # El parametro es el documento leido anteriormento
    drop.append('charges')
    x = document.drop(drop, 1)
    y = document['charges']
    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y, train_size=0.7, random_state=1)

    reg = LinearRegression().fit(x_train, y_train)
    return reg, x_test, y_test


def train_model_normalize(document, drop):
    std = StandardScaler()
    drop.append('charges')
    datos_normalizados = std.fit_transform(document)
    dataframe_normalizado = pd.DataFrame(
        datos_normalizados, index=document.index, columns=document.columns)
    # print(dataframe_normalizado)
    x = dataframe_normalizado.drop(drop, 1)
    y = dataframe_normalizado['charges']

    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y, train_size=0.7, random_state=1)

    #reg = LinearRegression().fit(x_train, y_train)
    #reg = Ridge(alpha=100).fit(x_train, y_train)
    #br = BayesianRidge()
    #reg = br.fit(x_train, y_train)
    #reg = Lasso(alpha=0.0000005, fit_intercept=False, tol=0.000000000000001,
    #      max_iter=1000000000).fit(x_train, y_train)
    reg = TweedieRegressor(alpha=0.1).fit(x_train,y_train)
    corr = x_train.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
                cmap=sns.diverging_palette(220, 10, as_cmap=True), square=True)
    return reg, x_test, y_test

def train_riesgo(document, drop):
    #datos_filtrados = document.loc[document['age'] >= 40]
    indices_riesgo = list()
    for indice, registro in document.iterrows():
        indice = 0
        if registro[4] == 1: 
            indice = indice + 10000 
        edad = registro[0] - 40
        if edad >= 1:
            indice = indice + (edad * edad)
        bmi = registro[2] - 25
        if bmi > 1:
            indice = indice + bmi * 400 
        indices_riesgo.append(indice)
    document['indice_riesgo'] = indices_riesgo
    datos_filtrados = document.loc[document['indice_riesgo'] < 10400]
    #datos_filtrados = datos_filtrados.loc[datos_filtrados['bmi'] < 25]
    #print(datos_filtrados)
    drop.append('charges')
    x = datos_filtrados.drop(drop, 1)
    y = datos_filtrados['charges']
    #print(x)

    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y, train_size=0.7, random_state=1)

    reg = LinearRegression().fit(x_train, y_train)
    #reg = Ridge(alpha=100).fit(x_train, y_train)
    #br = BayesianRidge()
    #reg = br.fit(x_train, y_train)
    #reg = Lasso(alpha=0.000005, fit_intercept=False, tol=0.00000001,
    #       max_iter=100000000).fit(x_train, y_train)
    #reg = TweedieRegressor(alpha=0.1).fit(x_train,y_train)
    return reg, x_test, y_test

# Los parámetros son: el modelo previamente entrenado y los datos de prueba


def test_model(reg, x_test, y_test):
    return reg.score(x_test, y_test)


def predict(reg, datos):  # Predice el resultado dado un conjunto de datos.
    return reg.predict(datos)


def ejecutar():
    document = read_doc('datos2.csv')

    eleccion = input(
        "¿Qué columnas desea ignorar?\nIntroduzcalas separadas con una coma.\n")
    # Indica qué variables va a ignorar para el modelo.
    drop = eleccion.split(',')

    #modelo, x_test, y_test = train_model(document, drop)
    #modelo, x_test, y_test = train_model_normalize(document, drop)
    modelo, x_test, y_test = train_riesgo(document, drop)

    y_predicted = predict(modelo, x_test)
    print("Error medio absoluto: {}.".format(
        str(metrics.mean_absolute_error(y_predicted, y_test))))
    print("Error medio al cuadrado: {}.".format(
        str(metrics.mean_squared_error(y_test, y_predicted))))
    print("Coeficiente de determinación: {}.".format(
        test_model(modelo, x_test, y_test)))

    fig, ax = plt.subplots()
    ax.scatter(y_predicted, y_test, edgecolors=(0, 0, 1))
    ax.plot([y_test.min(), y_test.max()], [
            y_test.min(), y_test.max()], 'r--', lw=3)
    ax.set_xlabel('Valor predecido')
    ax.set_ylabel('Valor verdadero')
    ax.set_title('Valores predecidos vs Valores verdaderos')
    plt.show()


if __name__ == "__main__":  # Ejecuta el programa.
    ejecutar()
