#pedir numeros a usr
numero = input(f'ingresar un numero: ')

#aca observamos que input siempre recibe string y resultado sera repetir la entrada 2 veces 
print(numero * 2) 

#para usarlo como numero se debe castear a int o float segun sea el caso
print(int(numero) * 2)
print(float(numero) * 2)