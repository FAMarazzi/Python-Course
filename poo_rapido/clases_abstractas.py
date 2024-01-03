from abc import ABC, abstractclassmethod

#esto sería una plantilla que no puede llamarse
#por ser abstracta y tampoco a sus métodos
#abstractos
class  Persona(ABC):
    
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.actividad=actividad
    
    #este método termina siendo obligatorio para
    #las subclases que creemos.
    #entonces debemos implementarlo y modificar
    #a gusto
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")
    

#no puedo hacer estudiante=Estudiante("Fede", 26, "Masculino", "Programación")        
        
class Estudiante(Persona):
    
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}")

class Trabajador(Persona):
    
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy trabajando de {self.actividad}")

estudiante= Estudiante("Fede", 26, "Masculino", "Programación")
estudiante.presentarse()
estudiante.hacer_actividad()
trabajador= Trabajador("Carlos", 61, "Femenino", "Obrero")
trabajador.presentarse()
trabajador.hacer_actividad()