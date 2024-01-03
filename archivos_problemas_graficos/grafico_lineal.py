import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("archivos_problemas_graficos\\estornudos.csv")

#creando el grafico
sns.lineplot(x="Fecha", y="Estornudos", data=df)

#creando un punto en el pico de mas pedos
plt.plot("01-06", 18,"o")

#mostrando grafico
plt.show()