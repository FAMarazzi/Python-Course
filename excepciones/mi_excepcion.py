class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
   
#lanzando mi propia excepción
raise MiExcepcion("Este es un error grave. Por favor, respete lo pedido")   

#manejandola
try:
    raise MiExcepcion("Ocurrió un error grave.")
except:
    print("Vuelva a intentarlo mas tarde.")
