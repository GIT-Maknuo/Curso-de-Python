n = [1,2,3,4,5,6,7,8,9]

#lambda funciones
multi= lambda x: x*2

print(multi(2))

#usando filter
def n_pares(num):
    if(num%2==0):
        return True

pares =  filter(n_pares,n)
print(list(pares))

#ejercicio anterior con lambda y filter
print(list(filter(lambda numeros: numeros%2==0, n)))
