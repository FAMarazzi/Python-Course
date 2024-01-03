#creo una función que verifica si el número dado
#es primo o no.
def es_primo(numero):
    
    #me encargo de retornar falso en los casos específicos
    if(numero==1 | numero==0):
        return False
    else:
        #verifico que el numero no pueda dividirse
        #por ningún numero entre 2 y él mismo
        for i in range(2, numero-1):
            #si es divisibler por alguno retorna False y terminaa el bucl,e
            if (numero%i==0): return False
        #si completó todo el bucle sin retornar false,
        #significa que es primo (devuelve True)
        return True

#función que devuelve una lista de todos
#los números primos entre 0 y ese número
def primos_hasta(numero):
    #creo una lista
    primos=[]
    for i in range(2,numero+1):
        #verifico si es primo y de ser asi
        #lo agrego a la lista
        if (es_primo(i)==True): 
            primos.append(i)
    
    #devuelvo la lista
    return primos

entrada=int(input("Bienvenido, ingrese un número y le daré una lista con todos los primos que hay entre el 0 y el número ingresado: "))
resultado=primos_hasta(entrada)
print(resultado)