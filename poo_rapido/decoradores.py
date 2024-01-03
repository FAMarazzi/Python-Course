#los decoradores modifican un poco una función
#le mando la función al decorador y le añade
#antes o después alguna funcionalidad adicional
def decorador(funcion):
    def funcion_modificada():
        print("Hacer esto antes de llamar a la función")
        funcion()
    
    return funcion_modificada

# def saludo():
#     print("Holus fede como va?")

# saludo_modificado=decorador(saludo)
# saludo_modificado()

#la forma correcta de
#usar un decorador es usando el @ previo a la declaración
#de la función que queremos "decorar"
@decorador
def saludo():
    print("Hola Bro, como va?")

saludo()