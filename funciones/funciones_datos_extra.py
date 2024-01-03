#creando una función de 3 parámetros

# def frase(nombre, apellido, adjetivo):
#     return f'Hola, vos sos {nombre} {apellido}, también llamado {adjetivo}?'

# frase_resultante=frase("Federico", "Marazzi", "crack")

# #utilizando keyword arguments
# frase_resultante=frase(apellido="Marazzi", adjetivo="capo", nombre="Fede")

#creando misma función con parámetro opcional y valor por defecto

def frase(nombre, apellido, adjetivo="boludín"):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante=frase("Fede", "Marazzi", "buen programador")
print(frase_resultante)