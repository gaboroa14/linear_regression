import csv
import matplotlib.pyplot as plt

with open('datos1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    elementos = list(csv_reader)
    edades = list()
    genero = list()
    imc = list()
    hijos = list()
    fumador = list()
    region = list()
    cargos = list()
    regiones = {
        'northeast': 0,
        'northwest': 1,
        'southeast': 2,
        'southwest': 3
    }
    for fila in elementos[1:]:
        edades.append(int(fila[0]))
        genero.append(0 if fila[1] == 'female' else 1)
        imc.append(float(fila[2]))
        hijos.append(int(fila[3]))
        fumador.append(1 if fila[4] == 'yes' else 0)
        region.append(regiones.get(fila[5]))
        cargos.append(float(fila[6].replace('.','')))
    print(region)
    plt.plot(edades)
    plt.show()