#conjunto lista componentes son variables o modificables
lista= ["Freddy","Python", True, 1.75] 
print(lista)
print(lista[0])
lista[2] = False
print(lista[2])

#conjunto tuple componentes son constantes no modificables
tupla= ("Freddy","Python", True, 1.75) 
print(tupla)
print(tupla[0])
#tupla[2] = False

#conjunto set componentes son constantes (no modificables e inaccesibles por indice, 
#no pueden duplicarse los elementos, estan desordenados)
conjunto = {"Freddy","Python", True, 1.75} 
print(conjunto)
# print(conjunto[0])

#diccionario (dict) es casi un json o un map en java (llave : valor )
diccionario={
    'nombre': "Freddy",
    'lenguaje': "Python",
    'activo': True,
    'altura': 1.75
}

print(diccionario["nombre"])
print(diccionario["activo"])





