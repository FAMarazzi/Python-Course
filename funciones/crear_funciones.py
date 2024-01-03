#una función simple
# def saludar():
#     print("Hola Fedu, vas bien con Python")
    
# saludar()

#función con parámetros
def saludar(nombre, genero):
    genero=genero.lower()
    if(genero=="mujer"):
        adjetivo="reini"
    elif(genero=="hombre"):
        adjetivo="brother"
    else:
        adjetivo="bebé"
        
    print(f'Hola {nombre}. Vas bien con Python {adjetivo}')
    
saludar("Fedu", "hombre")
saludar("Cami", "mujer")
saludar("Safiro", "no binarie")

#crear una función que retorne múltiples valores
def crear_contraseña_random(num):
    chars= "abcdefghij"
    num_string= str(num)
    num= int(num_string[0])
    c1= num -2
    c2=num
    c3=num-5
    contraseña= f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return contraseña, num

#desempaquetando la función (o desestructurando)
password, primer_numero= crear_contraseña_random(6273)

#mostrando los resultados obtenidos y el dato utilizado
print(f'Tu nueva contraseña generada de manera automática es: {password}')
print(f'El número clave utilizado para crearla fue: {primer_numero}')