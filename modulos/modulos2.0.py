import funciones_buenas.saludar  as func
import sys

print(func.saludar('freddy'))

#agregar modulo o funciones que se encuentra fuera del directorio
sys.path.append("d:\\Curso de Python\\funciones_buenas2")

print(sys.path)

import saludar2 as func2

print(func2.saludar('freddy'))


