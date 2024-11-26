frase = input("cuentame algo: ")
palabras =  len(frase.split(" "))

print(f'Dijiste {palabras} palabras en {palabras/2} segundos y otra persona tardaria {palabras/2*1.3}')

if palabras > 6:
    print('marico no hables tanta paja')