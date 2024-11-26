#funcion simple
def saludar():
    print("hola freddy")
#ejecutando funcion simple 
saludar()

#funcion con parametro de entrada
def saludar(nombre, sexo):
    sexo= sexo.lower()
    if sexo == "Mujer":
        print(f"hola {nombre} como estas chama")
    else:
        print(f"hola {nombre} como estas chamo")

#ejecutando funcion con parametro
saludar("FREDDY","M")
saludar("NAY", "MuJer")

def password(num):
    chars = "anmaoeprmtm"
    temp= str(num)
    num= int(temp[0])
    c1=num-2
    c2=num
    c3=num-5
    return (f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"), num

#desempaquetando la funcion
contra,primer_num =  password(981)

#mostrando lo retornado por la funcion
print(f'Tu contraseña nueva es: {contra}') 
print(f'El numero usado es: {primer_num}') 

#forma menos optima 
def sumaNO(lista):
    num = 0
    for number in lista:
        num = num + number
    return num

print(f'el resultado {sumaNO([4,9,1])}')

#optimo con tipo de parametro de entrada Args*
def suma(nom, *numeros):  
    return (f'{nom} la suma de tus numeros es {sum(numeros)}')

#forma de usar como *Args una lista
def suma_total(numbers):
    return sum([*numbers])

print(suma_total([4,9,1]))
print(suma("Freddy", 4,9,1))  
    