numeros=[1,2,3,4,5,6,7,8,9, 11, 24, 563, 131, 64, 67]

#creando una función lambda 
# que multiplica por 2 y devuelve el resultado
multiplicar_por_dos= lambda x : x*2

#creando función común que diga si un número
#es par o no
# def es_par(num):
#     if(num%2==0):
#         return True

#la función filter toma como parámetro una función
#que devuelve true o false y arma una lista
#con todos los valores que dieron true
#esos valores deben guardarse en una lista

# numeros_pares= filter(es_par, numeros)

#creando lo mismo que antes pero con lambda
numeros_pares= filter( lambda numero: numero%2==0, numeros)

print(list(numeros_pares))