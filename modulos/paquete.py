import paquete
import paquete.modulo_saludar as func
import paquete.modulo_saludar2

print(dir(paquete))

print(type(paquete))

print(paquete.__path__)

print(func.saludar('freddy'))

print(paquete.modulo_saludar2.saludar2('freddy'))

