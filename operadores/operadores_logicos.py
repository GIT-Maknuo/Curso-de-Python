#AND
lista_and =[
 True & True, #True
 True & False, #False
 False & True, #False
 False & False, #False
]

#OR 
lista_or =[
 True | True, #True
 True | False, #True
 False | True, #True
 False | False, #False
]

#NOT
lista_not =[not True, not False, not 2==2, not 2 > 29]

print(lista_and)
print(lista_or)
print(lista_not)