#lista creada con func list
list = list(['Freddy', 'Rengifo',34])
list2= (["agregando lista1 a lista2"])
clear_list= (["limpiar","lista"])
sort_list= ([4, 8, 1.1, 0])

#tamaño 
print(len(list))

#agregar elemento
list.append("append")
print(list)

#agrega elemento en posicion especifica
list.insert(2, "insert")
print(list)

#agregar varios elementos 
list.extend(["extend","eliminar con pop","eliminar con pop regresivo","eliminar con remove por valor"])
print(list)
list.extend(list2)
print(list)

#eliminando posicion de la lista por su indice, 
list.pop(6)
print(list)
#agragando indice negativo por ejemplo -1 podemos eliminar 
#comenzando por el ultimo indice
list.pop(-3)
print(list)

#eliminar elemento por su valor, "SI NO ENCUENTRA EL VALOR LANZA EXCEPCION"
list.remove('eliminar con remove por valor')
print(list)

#elimina todo lo de la lista
print(clear_list)
clear_list.clear()
print(clear_list)

#revierte la lista
print(sort_list)
sort_list.reverse()
print(sort_list)

#ordenar elementos (int,float,boolean),  elementos (string)d lanza excepcion
#ascendente
sort_list.sort()
print(sort_list)
#desendente
sort_list.sort(reverse=True)
print(sort_list)

#encotrar posicion de elemento dentro de lista, si no esta lanza excepcion
print(list.index(34))