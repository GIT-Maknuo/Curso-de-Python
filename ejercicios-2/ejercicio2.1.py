#compañeros    
def obterner_alumnos(cantidad):
    alums= []#creando lista
    for i in range(cantidad): #bucle para pedir la info
        nomb = input('ingrese nombre del alumno: ')
        edad = int(input('ingrese edad del alumno: '))
        alum = (nomb,edad)
        alums.append(alum)#añadiendo informacion a la lista
    alums.sort(key=lambda x: x[1])#ordenando de menor a mayor y asando lambda
    asistente= alums[0] [0] #accediendo a primer elemento ordenado
    profesor= alums[-1][0] #accediendo al ultimo elemento ordenado
    return asistente,profesor #retornando una tupla con ambos 

asistente, profesor= obterner_alumnos(5) #desempaquetando 

print(f'El profe es {profesor} y su assitente {asistente}')


