import csv

with open ("archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    #print(csv.reader(archivo))
    #print("archivo leido correctamente")
    for row in reader:
        print(row)