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


def train_model_normalize(document,drop):
    std = StandardScaler()
    drop.append('charges')
    print(document)
    datos_normalizados = std.fit_transform(document)
    dataframe_normalizado = pd.DataFrame(datos_normalizados, index=document.index, columns=document.columns)
    #print(dataframe_normalizado)
    x = dataframe_normalizado.drop(drop, 1)
    y = dataframe_normalizado['charges']

    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y, train_size=0.7, random_state=1)

    reg = LinearRegression().fit(x_train, y_train)
    #reg = Ridge(alpha=100).fit(x_train, y_train)
    #br = BayesianRidge()
    #reg = br.fit(x_train, y_train)
    #reg = Lasso().fit(x_train, y_train)
    #reg = TweedieRegressor().fit(x_train,y_train)
    corr = x_train.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True), square=True)
    return reg, x_test, y_test

# Los parámetros son: el modelo previamente entrenado y los datos de prueba


def test_model(reg, x_test, y_test):
    return reg.score(x_test, y_test)


def predict(reg, datos):  # Predice el resultado dado un conjunto de datos.
    return reg.predict(datos)


def ejecutar():
    document = read_doc('datos_git_region.csv')

    eleccion = input(
        "¿Qué columnas desea ignorar?\nIntroduzcalas separadas con una coma.\n")
    # Indica qué variables va a ignorar para el modelo.
    drop = eleccion.split(',')

    #modelo, x_test, y_test = train_model(document, drop)
    modelo, x_test, y_test = train_model_normalize(document,drop)

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
