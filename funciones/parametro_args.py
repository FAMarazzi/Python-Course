# forma no optima
# def suma(lista):
#     numeros_sumados=0
#     for numero in lista:
#         numeros_sumados= numeros_sumados + numero
#     return numeros_sumados
# print(suma([1,2,3,4,5]))

#forma óptima de sumar valores (no la mejor) usando operador args (*)
#usa el operador args para retornar
#de esta forma la lista retorna todos los valores sin un for.
def suma_total(numeros):
    return sum([*numeros])

resultado=suma_total([2,5,7,12,31,22])

#utilizando el operador args (*) como argumento
#es la forma más óptima y que mas se usa.
#el * debe ser el último ya que indica que todos los
#parámetros siguientes entraran como numeros

def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus números es {sum(numeros)}"

resultado2=suma("Federico", 2, 5, 1, 66)
print(resultado2)

