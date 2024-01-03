#cambiar el tipo de dato de una columna
import pandas as pd
df= pd.read_csv("archivos_problemas\\datos.csv")

#convertir a string los datos de una columna
df["edad"]=df["edad"].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df["edad"][0]))

#reemplazar los datos "fede por el mas crack"
df['apellido'].replace("marazzi", "apellido god", inplace=True)

#eliminando las filas que contengan datos faltantes
df=df.dropna()

#eliminar filas repetidas
df=df.drop_duplicates()

#crear un csv con el dataframe resultante (teniendo los datos limpios)
df.to_csv("archivos_problemas\\datos_limpios.csv")

print(df)