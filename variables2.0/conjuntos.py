#conjunto con set
#set puede contener elementos inmutables como elementos tuple, 
# si colocamos conjuntos modificables da excepcion
conjunto = set(["dato1","dato2",("datTuple1","datTuple2")])
print(conjunto)

#para meter conjunto inmutables dentro de conjunto inmutables
conj1=frozenset(["dato1","dato2"])
conj2={conj1,"dato3"}

print(conj2)

#teorias de conjuntos
conj1 = {1,3,5,7}
conj2 = {1,3,7}
conj3={4}

#SUBCONJUNTO DE:
#todos los elementos de 2 estan en 1 en este caso TRUE
print(conj2.issubset(conj1))
print(conj2<=conj1)
#todos los elementos de 1 estan en 2 en este caso FALSE
print(conj1.issubset(conj2))
print(conj1<=conj2)

#SUPERCONJUNTO DE:
#todos los elementos de 2 estan en 1super en este caso FALSE
print(conj2.issuperset(conj1))
print(conj2 > conj1)
#todos los elementos de 1 estan en 2super en este caso TRUE
print(conj1.issuperset(conj2))
print(conj1 > conj2)

#verificar con disjoint si por lo menos hay un elemento 
# en el conjunto con que se compara FALSE
print(conj1.isdisjoint(conj3))# es totalmente diferente TRUE
print(conj2.isdisjoint(conj1))# es totalmente diferente FALSE
