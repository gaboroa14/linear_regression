import csv

with open('datos_git.csv') as csv_file:
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
    result_file = open("datos_git_region.csv",'w')
    wr = csv.writer(result_file, dialect='excel')
    for elemento in nuevos_datos:
        wr.writerow(elemento)