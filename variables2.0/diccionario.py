#creando diccionario con dict
diccionario = dict(nombre="Freddy", apellido="Rengifo" )

print(diccionario)

dicc2 = {("tupla","test"):"se puede"}
print(dicc2)

dicc3 = {frozenset(["tupla","test"]):"se puede"}
print(dicc3)

#creando diccionarios con fromkeys
dicc4 = dict.fromkeys(["edad","sexo","fecha"])
print(dicc4)

dicc5 = dict.fromkeys(["edad","sexo","fecha"],"asig val")
print(dicc5)