#crear una lista con list()

lista= list(["hola", "Fede", 21, 1999, True])

# devuelve la cantidad de elementos de la lista
cantidad_elementos=len(lista)

#agrega un elemento al final de la lista

lista.append("HOLA HERMANO")

#agreega un elemento a la lista en un índice especificado

lista.insert(2, "INSERTADO")

#agrega varios elementos al final de una lista
#enviando otra lista de elementos

lista.extend([False, 2032])

#elimina un elemento de la lista (por índice)

lista.pop(3)

#elimina un elemento por su valor

lista.remove(False)

#elimina todos los elementos de una lista
#lo dejamos comentado para evitar eliminación

#lista.clear()

# Ordena la lista de forma ascendente (sólo numeros requeridos)
#comento para evitar cambiar lista

lista=[4, 2,21, 12, 4312]
lista.sort()


#invierte la lista
lista.reverse()

#verificando si un elemento se encuentra en la lista

#elemento_encontrado= lista.index(1997)

#NO TODAS LAS ANTERIORES FUNCIONAN PARA TUPLAS
#NI TAMPOCO PARA CONJUNTOS SET

print(lista)
