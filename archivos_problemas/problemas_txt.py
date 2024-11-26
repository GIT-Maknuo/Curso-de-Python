nombres = ["freddy","alex","hector","jairo","jose"]
apellidos = ["rengifo","legon","reyes","leon","camargo"]

#registrar en txt
with open("resolviendo_problemas//nombres_y_apellidos.txt","w") as archivo:
    archivo.writelines("Los datos son:\n\n")
    [archivo.writelines(f"nombre:{n}\napellido:{a}\n---------------\n") for n,a in zip(nombres, apellidos)]