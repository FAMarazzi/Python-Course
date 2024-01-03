#Ejercicio: CLASE Estudiante con atributos nombre edad 
# y grado
#metodo estudiar() indicando que está estudiando.
#Objeto estudiante para usar este metodo.
#Se debe interactuar con el usuario para recibir sus atributos

class Estudiante:
    
    def __init__(self, nombre, edad, grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando...")

nombre=input("Buen día estudiante, ingrese su nombre: ")
edad=input("Ingrese su edad: ")
grado=input("Ingrese su grado: ")

estudiante=Estudiante(nombre, edad, grado)


print(f"""
      Datos del estudiante:\n
      ---------------------
      Nombre: {estudiante.nombre}
      ---------------------
      Edad: {estudiante.edad}
      ---------------------
      Grado: {estudiante.grado}"""
      )

estudiar= input("Qué desea hacer?")
if(estudiar.lower()== "estudiar"):
    estudiante.estudiar()
