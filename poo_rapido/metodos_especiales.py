class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        
    #sobrecargando métodos
    #con esta función redefino como va a mostrarse
    #la clase cuando lo escribamos como string.
    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'

    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'

    #esta función la usamos para añadir una funcionalidad
    #en este caso estamos añadiendo que se puedan sumar
    #dos objetos personas. y que se comporte
    #de laa forma indicada
    #suma edades, y concatena nombres.
    def __add__(self,otro):
        nuevo_valor=self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)

fede=Persona("Fede", 26)

#Ahora el print me muestra Persona(nombre=Fede, edad=26)
print(fede)


#para usar el repr usamos
repre=repr(fede)

#esta función usando la representación
#hace quee podamos llamar a los valores indiv.
resultado=eval(repre)

print(resultado.nombre)

maria=Persona("María", 63)

#por ultimo al usar el add
nueva_persona= fede + maria
print(nueva_persona)