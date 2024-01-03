class Persona():
    def __init__(self, nombre, edad):
        #el _ es un concenso de que algo es privado
        #como si fuera protegido
        self.__nombre =nombre
        self._edad=edad
        #ambos deberían usar
        
        #el doble (__) es algo privado realmente
        #(no se puede acceder sin getter ni setter)
        #de todas formas ambos deberían usarlos
    
    #el decorador property me permite llamar
    #a un getter sin los parentesis como si
    #fuera una propiedad,
    #además de poder llamarlo nombre solamente
    @property    
    def nombre(self):
        return self.__nombre
    
    #el decorador "".setter
    #me permite llamarlo solamente nombre y usarlo
    #como si fuera una prop
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre
        
    #lo siguiente sería un deleter
    #esto eliminaría la propiedad original __nombre
    @nombre.deleter
    def nombre(self):
        del self.__nombre
        
    def __hablar(self):
        print("Hola, como estas?")

    
fede= Persona("Federico", 26)

#el decorador permite que no use () 
#al llamar a get_nombre
print(fede.nombre)

fede.nombre="FRANCO"

nombre=fede.nombre
print(nombre)

del fede.nombre
print("Hola jaja")
#y ahora lanzaría error porque ya no existe.
#print(fede.nombre)

#el de abajo sería privado en serio y tiraría excepcion
#objeto.__hablar()

