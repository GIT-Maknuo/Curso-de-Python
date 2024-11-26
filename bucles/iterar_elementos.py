animales=["gato","perro","loro","cocodrilo"] #listas
numeros=(2,4,7,9)#tuplas
diccionario = dict(nombre="Freddy", apellido="Rengifo" )
cadena = 'hola freddy'

for animal in animales:
    print(f"El animal es: {animal}")
    
for numero in numeros:
    print(f"{numero} multiplicado por 2 es: {numero *2}")
    
#iterar las dos listas simultaneamente con "ZIP" 
# condicion debe tener la misma cantidad de elementos
for numero, animal in zip(animales, numeros):
    print(f"El animal es: {animal}")
    print(f"El numero es: {numero}")
    
#usando range
for num in range(2,5):
    print(num)
    
for num in range(5):
    print(num)
    
#usando enumerate
for num in enumerate(numeros):
    print(num)
    print(f"indice {num[0]} valor {num[1]}")
#usando else
else:
    print("termino")

#con diccionario    
for key in diccionario.items():
    print(key)
    print(f"key es {key[0]} valor {key[1]}")
    
#cmbinando if con iterar
for animal in animales:
    if animal== 'cocodrilo':
        continue
    print(f'{animal} es domestico')

for animal in animales:
    if animal== 'cocodrilo':
        break
    print(f'{animal} es domestico')
print(f'coreeeee {animal}')

for char in cadena:
    print(char)
    
lista_numeros_x_dos= [x*2 for x in numeros]
print(lista_numeros_x_dos)