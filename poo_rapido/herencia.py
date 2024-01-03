class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
        
    def hablar(self):
        print("Hola, como soy una persona, puedo hablar")

#de esta forma puede heredar la clase persona
#siendo persona su clase "padre"    
class Empleado(Persona):
    #el constructor debe tener todos los anteriores
    #asignados y luego los propios
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo=trabajo
        self.salario=salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, promedio, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.promedio=promedio
        self.universidad=universidad
        
empleado=Empleado("Fede", 26, "Argentino", "Profe", "Esa información es privada")
estudiante=Estudiante("Fede", 26, "Argentino", 8.33, "UBA")
print(estudiante.promedio)
print(estudiante.nombre)
estudiante.hablar()