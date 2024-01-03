class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando porque puedo hablar")
   
class Artista:
    def __init__(self, habilidad):
        self.habilidad=habilidad
        
    def getHabilidad(self):
        return self.habilidad

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario=salario
        self.empresa=empresa
    
    def presentarse(self):
        return f'Hola, soy: {self.nombre}, mi habilidad es {self.getHabilidad()} y trabajo en {self.empresa}'
        
empleado_artista=EmpleadoArtista("Fedu", 26, "Argentino", "Cojer Mucho", "1600000", "ET.35")
roberto=Artista("Cantar")

print(empleado_artista.getHabilidad())
print(empleado_artista.presentarse())

herencia= issubclass(EmpleadoArtista, Persona)
instancia= isinstance(roberto, Artista)
print(instancia)