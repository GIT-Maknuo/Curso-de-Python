#abrir file
with open('archivos\\texto.txt',encoding='UTF-8') as archivo:
    #leer y no es necesario cerrar con with open
    print(archivo.read())