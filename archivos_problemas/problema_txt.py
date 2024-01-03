#Tengo los nombres y los apellidos en dos listas separadas.
#Quiero recorrerlos en un mismo print y escribirlos en un txt de forma óptima

#creo las 2 listas
nombres=["Federico", "Camila", "Sabrina", "Alejandra", "Mariela"]
apellidos=["Marazzi", "Marazzi", "Zamira", "Permiso", "Castaldini"]

#registro esta información en un txt
#si no está creado, lo crea.
with open("archivos_problemas\\nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres, apellidos)]
    