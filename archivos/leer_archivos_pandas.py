import pandas as pd

#print(type(pd))

#leyendo archivo y generando data frame
df =  pd.read_csv("archivos\\datos.csv")
#obteniendo valore de columna nombre
nombres = df["nombre"]
print(nombres)

#ejemplo de leer asignarles otros nombres a las columnas
df2 =  pd.read_csv("archivos\\datos.csv", names=["names","lastname","age"])
print(df2)

#ejemplo de slicing
cadena = "0123456789"
print(cadena[2:5])

#ejemplo ordenar df por al valores de algun campo en particular
df_asc = df.sort_values("edad")
df_des = df.sort_values("edad",ascending=False)

print(df_asc)
print(df_des)

#ejemplo concatenar listas
concat =  pd.concat([df_des, df_asc])
print(concat)

#ejemplo tomar filas desde la cabeza
print("filas desde la cabeza")
print(df_asc.head(3))

#ejemplo tomar filas desde pie
print("filas desde pie")
print(df_asc.tail(3))

#ejemplo mostrar caracteristicas de la informacion 'filas y columnas'
caracteristicas = df.shape #tupla
print(f'caracteristicas {caracteristicas}')
print(f'filas {caracteristicas[0]}')
print(f'columnas {caracteristicas[1]}')

filas , columnas = caracteristicas # desempaquetando

#info estadisticas 
print(df.describe())

#accediendo a elemento especifico con loc
element = df.loc[2, "edad"]
print(element)

#accediendo a elemento especifico con iloc 'filas, colum' 
element = df.iloc[2, 2]
print(element)

#accediendo a elementos de fila o columna con iloc 'filas, colum'
all_element = df.iloc[:,0]
print(all_element)

#accediendo a elemento especifico con loc y condicional
element = df.loc[df["edad"]>40, :]
print(element)