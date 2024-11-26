import pandas as pd

#cambiar tipo de datos de una columna
df = pd.read_csv("resolviendo_problemas//datos.csv")
print(type(df["edad"][0]))

df["edad"] = df["edad"].astype(str)
print(type(df["edad"][0]))

#reemplazar valor
df["apellido"].replace("rengifo","legon",inplace=True)
print(df["apellido"])

#eliminar filas que posean datos repetidos
df = df.drop_duplicates()
print(df)

#eliminar filas que posean datos incompletos
df = df.dropna()
print(df)

#creando csv limpio
df.to_csv("resolviendo_problemas//datos.csv(limpio)")

