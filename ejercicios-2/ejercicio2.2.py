#creando funcion que retorne numeros primos
def es_primo(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

print(es_primo(13))


def primos_hasta(num):
    primos = []
    for i in range(3,num+1):
        if es_primo(i):
            primos.append(i)
    return primos

print(primos_hasta(13))

def fibonacci(num):
    a,b=0,1
    res = [0]
    for i in range(num):  
        if a + b > num : 
            return res     
        else:
            res.append(b)
            a,b = b, a+b

print(fibonacci(20))


