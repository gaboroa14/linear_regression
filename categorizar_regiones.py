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

import csv

# Este script genera un nuevo archivo csv en que se desglosan las regiones en variables categóricas.
# Así, en lugar de tener una sola variable región que puede ser 0, 1, 2 o 3, se tienen 4 variables
# asociadas a cada región (ne, nw, se, sw) que indican la pertenencia o no a las mismas.

with open('datos1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    datos = list(csv_reader)
    nuevos_datos = list()
    datos[0].append('ne')
    datos[0].append('nw')
    datos[0].append('se')
    datos[0].append('sw')
    print(datos[0])
    for row in datos[0:]:
        if row[5] == '0':
            row.append('1')
            row.append('0')
            row.append('0')
            row.append('0')
        elif row[5] == '1':
            row.append('0')
            row.append('1')
            row.append('0')
            row.append('0')
        elif row[5] == '2':
            row.append('0')
            row.append('0')
            row.append('1')
            row.append('0')
        else:
            row.append('0')
            row.append('0')
            row.append('0')
            row.append('1')
        nuevos_datos.append(row)
        print(row)
    result_file = open("datos2.csv",'w')
    wr = csv.writer(result_file, dialect='excel')
    for elemento in nuevos_datos:
        wr.writerow(elemento)