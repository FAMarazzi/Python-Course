#falto el profe y los pibes arman la clase

#función que obtiene asistente y profesor según la edad
def obtener_compañeros(cantidad):
    
    #inicializo lista compañeros
    compañeros=[]
    
    #for para pedir info de cada compa
    for i in range(cantidad):
        nombre=input("Ingrese el nombre del compañero: ")
        edad=int(input(f"Ingrese la edad del compañero {nombre}: "))
        compañero=(nombre, edad)
        
        #agrego listas de nombre y edad en lista compañeros
        compañeros.append(compañero)
        
    #ordeno de menor a mayor según edad    
    compañeros.sort(key=lambda x:x[1])
    
    #accedemos al nombre del primero y del último para definir
    #asistente y profesor
    asistente= compañeros[0][0]
    profesor= compañeros[-1][0]
    
    #retornamos una tupla
    return asistente, profesor

#desempaquetamos la tupla para guardar los retornos de la función
asistente, profesor= obtener_compañeros(3)
  
#mostramos resultados obtenidos
print(f'El compañero que hará de profesor será: {profesor} y el asistente será: {asistente}')