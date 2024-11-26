numeros = [4,7,1,8,9]

#encontrando mayor y menor
print(max(numeros))
print(min(numeros))

#redondeando decimales con round
print(round(123.123456789, 2))

#validar si elemento o objeto esta "vacio, none, False 0" --> False
#devolvera True si parametro  es distinto a a los anteriores mensionados 
print(bool(0))
print(bool(False))
print(bool([]))
print(bool(""))
print(bool(-1))# True

#valida todo el contenido de una lista retorna True si todos los elementos 
#son didstintos a "vacio, none, False 0" 
print(all([1,2,"abc",[2,3]]))#true
print(all([1,2,"",[2,1]]))#false

#suma los valores de un iterable
print(sum(numeros))

