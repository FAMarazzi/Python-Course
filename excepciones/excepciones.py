def sumar_dos():
    #inicio un bucle
    while True:
        #pidiendo numeros
        a= input("Numero 1: ")
        b= input("Numero 2: ")
        
        #intentamos convertirlos a entero y sumarlos
        try:
            resultado=int(a)+int(b)
            
        #si lanza excepción, destaco el error y
        #se reinicia el loop para pedir nuievamente numeros
        except ValueError as e:
            print("Por favor, ingrese dos números")
            print(f"ERROR: {e}")
            
        #si todo sale bien termino el bucle
        else:
            break
        
        #el finally se ejecuta siempre pero no se suele usar mucho
        finally:
            print("Esto se ejecuta siempre")
    
    #muestro el resultado
    return resultado

print(sumar_dos())