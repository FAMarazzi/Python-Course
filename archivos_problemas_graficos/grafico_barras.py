import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")

#creando el grafico de barras
sns.barplot(x="Fuente", y="Ingresos", data=df)

#sumando el total de ingresos
total_ingresos=df["Ingresos"].sum()

#mostrando el total de ing por consola
print(f'El total de ingresos es de: ${total_ingresos} USD')

#mostrando grafico
plt.show()