#creando un conjunto con set()
#se debe pasar una lista a la función set creando asi el cjto.

conjunto= set(["dato1"])

#metiendo un conjunto dentro de otro cjto
conjunto1=frozenset(["dato 1", "dato 2"])
conjunto2={conjunto1, "dato 3"} ##también podría crearse con set

print(conjunto2)

#teoria de conjuntos

conjunto1={1,3,5,7}
conjunto2={1,3,7}

#verificando si es un subconjunto
resultado=conjunto2.issubset(conjunto1)
resultado= conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado= conjunto2.issuperset(conjunto1)
resultado= conjunto2 > conjunto1

#verifica si no hay ningún número en común
#daría true si ningún elemento coincide.
resultado=conjunto2.isdisjoint(conjunto1)

print(resultado)