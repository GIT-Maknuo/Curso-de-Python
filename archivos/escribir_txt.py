#abrir file y escribir dandole permiso de escritura con 
#sobreescribir 'w'
#with open('archivos\\texto.txt', 'w' ,encoding='UTF-8') as archivo:
#agregar lineas 'a'
with open('archivos\\texto.txt', 'w' ,encoding='UTF-8') as archivo:
    #sobreescribir el archivo
    #archivo.write('nueva linea')
    #escribir o agregar lineas
    #archivo.writelines(['nueva linea1\n', 'nueva linea2'])
    #archivo.writelines(['\nnueva linea3\n', 'nueva linea4'])
    for i in range(5):
        archivo.write(f"\n linea {i+1} agregada \n")