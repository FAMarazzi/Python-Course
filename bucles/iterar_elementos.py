animales=["pez", "gato", "perro", "mono", "cisne"]
numeros=[12, 512, 123, 563, 141]

#recorrer la lista animales
for animal in animales:
    print(f'La variable animal en este momento es igual a: {animal}')
    

#iterando dos listas del mismo tamaño al mismo tiempo
for animal, numero in zip(animales, numeros):
    print(f"recorriendo lista 1: {animal}")
    print(f'Recorriendo lista 2: {numero}')
    
#forma no óptima de recorrer una lista con su indice (no funciona en conjuntos)
#la función range arma un rango entre 0 y el numero enviado por parámetro
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su índice
for num in enumerate(numeros):
    indice=num[0]
    valor=num[1]
    print(f'El índice es {indice}. El valor es {valor}')
    
#usando el for/else
for numero in numeros:
    print(f'ejecutando el último bucle del archivo, valor actual: {numero}')
else:
    print("Esto se ejecuta al finalizar y salir del bucle")
    
#todo lo anterior funciona exactamente igual para tuplas y conjuntos