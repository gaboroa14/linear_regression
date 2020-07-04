import csv
import matplotlib.pyplot as plt
import statistics as esta
from scipy import stats as estasc

def generar_diccionario():
    with open('datos1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        elementos = list(csv_reader)
        regiones = {
            'northeast': 'ne',
            'northwest': 'nw',
            'southeast': 'se',
            'southwest': 'sw'
        }
        dic = {
            'h_f_ne' : [],
            'm_f_ne' : [],
            'h_n_ne' : [],
            'm_n_ne' : [],
            'h_f_nw' : [],
            'm_f_nw' : [],
            'h_n_nw' : [],
            'm_n_nw' : [],
            'h_f_se' : [],
            'm_f_se' : [],
            'h_n_se' : [],
            'm_n_se' : [],
            'h_f_sw' : [],
            'm_f_sw' : [],
            'h_n_sw' : [],
            'm_n_sw' : [],
        }
        genero = {
            'male' : 'h',
            'female' : 'm'
        }
        fumador = {
            'yes' : 'f',
            'no' : 'n'
        }
        for fila in elementos[1:]:
            region = regiones.get(fila[5])
            fum = fumador.get(fila[4])
            gen = genero.get(fila[1])
            categoria = ''.join([gen,'_',fum,'_',region])
            dic[categoria].append({
                'edad': int(fila[0]),
                'imc': float(fila[2]),
                'hijos': int(fila[3]),
                'cargos': float(fila[6].replace('.',''))
            })
    return dic

def Medias(dic):
    #Calcular las medias de Las edades de las variables
    edades = list()
    for elemento in dic:
        categoria = (dic[elemento])
        for fila in categoria:
            edades.append(fila['edad'])
        print(elemento)
        print(esta.mean(edades))

dic = generar_diccionario()

#Medias(dic)

#def Medianas(dic):
    #Calcular las medianas de las edades 

def Modas(dic):
    for elemento in dic:
        categoria = (dic[elemento])
        edades = list()
        for fila in categoria:
            edades.append(fila['edad'])
        moda = "La moda de la edad de la categoría {} es el valor {} con {} apariciones."
        print(moda.format(elemento, str(estasc.mode(edades)[0][0]),str(estasc.mode(edades)[1][0])))
    for elemento in dic:
        categoria = (dic[elemento])
        edades = list()
        for fila in categoria:
            edades.append(fila['imc'])
        moda = "La moda de la imc de la categoría {} es el valor {} con {} apariciones."
        print(moda.format(elemento, str(estasc.mode(edades)[0][0]),str(estasc.mode(edades)[1][0])))
    for elemento in dic:
        categoria = (dic[elemento])
        edades = list()
        for fila in categoria:
            edades.append(fila['hijos'])
        moda = "La moda de los hijos de la categoría {} es el valor {} con {} apariciones."
        print(moda.format(elemento, str(estasc.mode(edades)[0][0]),str(estasc.mode(edades)[1][0])))
    for elemento in dic:
        categoria = (dic[elemento])
        edades = list()
        for fila in categoria:
            edades.append(fila['cargos'])
        moda = "La moda de los cargos de la categoría {} es el valor {} con {} apariciones."
        print(moda.format(elemento, str(estasc.mode(edades)[0][0]),str(estasc.mode(edades)[1][0])))

def Medianas(dic):
    for elemento in dic:
        categoria = (dic[elemento])
        edades = list()
        for fila in categoria:
            edades.append(fila['edad'])
        mediana = "La mediana de la edad de la categoría {} es el valor {}."
        print(mediana.format(elemento, str(esta.median(edades))))
    for elemento in dic:
        categoria = (dic[elemento])
        edades = list()
        for fila in categoria:
            edades.append(fila['imc'])
        mediana = "La mediana de la imc de la categoría {} es el valor {}."
        print(mediana.format(elemento, str(esta.median(edades))))
    for elemento in dic:
        categoria = (dic[elemento])
        edades = list()
        for fila in categoria:
            edades.append(fila['hijos'])
        mediana = "La mediana de los hijos de la categoría {} es el valor {}."
        print(mediana.format(elemento, str(esta.median(edades))))
    for elemento in dic:
        categoria = (dic[elemento])
        edades = list()
        for fila in categoria:
            edades.append(fila['cargos'])
        mediana = "La mediana de los cargos de la categoría {} es el valor {}."
        print(mediana.format(elemento, str(esta.median(edades))))
Medianas(dic)