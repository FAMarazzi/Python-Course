frutas= ["banana", "manzana", "durazno", "frutilla", "ciruela", "sandía", "naranja"]
cadena= "Hola Fedu"
numeros= [2,4,5,6,9]

#evitando que se coma una manzana con la secuencia continue
#continue hace que el for saltee al proximo ciclo

for fruta in frutas:
    if fruta=="manzana":
        continue
    print(f'Voy a comer una {fruta}')
    
#evitar que el bucle siga ejecutándose (el else del bucle tampoco se ejecutaría)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta=="ciruela":
        print(f'La ciruela me cayó mal, mejor voy a dejar de comer')
        break
else:
    print("Ciclo terminado")
    
#recorriendo una cadena de texto
for caracter in cadena:
    print(caracter)
    
#for en una sóla linea de código duplicando los números
numeros_duplicados= [x*2 for x in numeros]
print(numeros_duplicados)
    