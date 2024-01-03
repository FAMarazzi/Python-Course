class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def mostrar_nombre_edad(self):
        print(f"Nombre: {self.nombre}\n")
        print(f"Edad: {self.edad}\n")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado=grado
        
    def mostrar_grado(self):
        print(f"Grado: {self.grado}\n")

estudiante=Estudiante("Federico", 26, "10mo")
estudiante.mostrar_nombre_edad()
estudiante.mostrar_grado()