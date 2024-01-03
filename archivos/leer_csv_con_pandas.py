import pandas as pd

#uso la funcion read_csv para leer el archivo csv
#df es por data frame
df= pd.read_csv("archivos\\datos.csv")
df2= pd.read_csv("archivos\\datos.csv")

#obtengo los datos de la columna nombre
nombres=df["nombre"]

#ordeno el dataframe por la edad
df_edad_ascendente=df.sort_values("edad")

#ordeno de forma descendente
df_edad_descendente=df.sort_values("edad", ascending=False)

#concateno 2 dataframes
df_concatenado=pd.concat([df, df2])

#accedo a las primeras 3 filas con head
primeras_filas=df.head(3)

#accedo a las ultimas 3 con tail
ultimas_filas=df.tail(3)

#la propiedad shape del data frame guarda un array con las filas y columnas que tiene
#lo desestructuro en dos datos separados
filas_totales,columnas_totales= df.shape

#obteniendo data stadistics del dataframe (importante para analisis de datos)
df_info=df.describe()

#accediendo a la edad de la fila 2. propiedad loc
#fila, columna
elemento_especifico_loc=df.loc[2, "edad"]

##accediendo a la edad de la fila 2. propiedad iloc (por índice)
elemento_especifico_iloc=df.iloc[2,2]

#accediendo a todos los apellidos con loc
#los dos puntos funcionan como el slice método con caracteres o listas para cortar
apellidos_loc= df.loc[:, "apellido"]

#podria hacer un slice de 1 y desde el uno seleccionar 3 incluyendolo. 
apellidos_1a3=df.loc[1:3, "apellido"]

#obtener los apellidos con iloc
apellidos_iloc=df.iloc[:,1]

#fila 3 con loc
fila_3=df.loc[2, :]

#fila 3 con iloc sería igual (pues el primero siempre es indice)
fila_3=df.iloc[2, :]

#accediendo a filas con edades mayores a 30
mayor_que_30= df.loc[df["edad"]>30, :]

print(mayor_que_30)
