cadena1="Freddy, Rengifo "
cadena2="Bienvenido"
cadena3="33"

#resultados de metodos para string
res = [
    cadena1.lower(), #transforma minuscula
    cadena1.upper(), #transforma mayuscula
    cadena1.capitalize(), #coloca primera letra del string en May
    cadena1.find(" "), #encuentra pocision de caracter 
    cadena1.find("u"), #encuentra pocision de caracter si no esta devuelve -1
    cadena1.index("y"),  #encuentra pocision de caracter
    #cadena1.index("u"),  #encuentra pocision de caracter devuelve excepcion
    cadena3.isnumeric(), #True si es numerico False si no lo es
    cadena1.isnumeric(), #True si es numerico False si no lo es
    cadena3.isalpha(), #True si es alfabetico False si no lo es
    cadena2.isalpha(), #True si es alfabetico False si no lo es
    cadena1.count("e"), #coincidencias de caracter en string
    len(cadena2), #tamaño de la cadena
    cadena1.startswith("Fre"), #True si string comienza asi
    cadena3.replace("3", "a") #ubica y reemplaza 
    ]
split = cadena1.split(",")

print(res)
print(split)