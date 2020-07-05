import csv

with open('datos1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    datos = list(csv_reader)
    nuevos_datos = list()
    for row in datos[0:]:
        row[6] = row[6].replace('.','')
        print(row)
        nuevos_datos.append(row)
    result_file = open("nombres.csv",'w')
    wr = csv.writer(result_file, dialect='excel')
    for elemento in nuevos_datos:
        wr.writerow(elemento)