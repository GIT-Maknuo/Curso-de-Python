archivo = open('archivos\\texto.txt',encoding='UTF-8')
#leer archivo completo
#print(archivo.read())

#leer archivos por lineas
lineas= archivo.readlines()
print(lineas)

#leer linea "readline()" o cantidad de caracteres de una linea "readline(10)"
#linea= archivo.readline()
#linea= archivo.readline()
#print(linea)

#cerrar archivo 'importante'
archivo.close()