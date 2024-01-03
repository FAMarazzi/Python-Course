numeros= [4,7,18,12,3]

#maximo
numero_mas_alto=max(numeros)

#minimo
numero_mas_bajo=min(numeros)

#redondeando a 3 decimales
numero=round(12.345678, 3)

#bool retorna 
# False -> 0, Vacio, False, None.
# True -> distinto a 0, Dato no vacío, True, Cadena.
resultado_bool=bool("asdad")

#all retorna true si todos los valores de la lista son verdaderos
resultado_all=all([1,True, "w", 1])

#suma todos los valores de un iterable
suma_total= sum(numeros)

print(suma_total)

#LAS FUNCIONES SUM MAX Y MIN DEVUELVEN
#EXCEPCIONES SI NO SON NÚMEROS