#importar funciones o metodos 'mudulos' de otra clase o archivo 
# 'as' asignar pronombre
import modulo_saludar as func

#accediendo a solo funciones necesarias 
from modulo_saludar import saludar2, saludar 

#contenido
print(dir(func))

#usando el pronombre
print(func.saludar('freddy'))

#accediendo a solo funciones necesarias 
print(saludar2('Freddy'))
print(saludar('Freddy'))