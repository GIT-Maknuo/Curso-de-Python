diccionario={
    'nombre': "Freddy",
    'lenguaje': "Python",
    'activo': True,
    'subscription': 1000000
}
print(diccionario)
#obtener elemento del diccionario, si no lo encuentra lanza excepcion
print(diccionario['lenguaje'])
#obtener elemento del diccionario, si no lo encuentra "NONE"
print(diccionario.get('sssss'))  

#aplica metodos (pop , clear)

#obteniendo elementos iterables
print(diccionario.items())