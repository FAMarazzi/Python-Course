#Principio de segregación de interfaz
#Ningun cliente debe ser forzado a depeender
#de interfaces que no utilizamos.
from abc import ABC, abstractmethod

#si creo la siguiente interfaz o clase abstracta
# y necesito englobar a robots trabajadores
#estaría cometiendo un error ya que los robots
#no podrían comer ni dormir entonces debemos
#aplicar el metodo de segregación de interfaces.
# class Trabajador(ABC):
    
#     @abstractmethod
#     def comer(self):
#         print("El humano está comiendo")
    
#     @abstractmethod
#     def trabajar(self):
#         print("El humano está trabajando")
    
#     @abstractmethod
#     def dormir(self):
#         print("El humano está durmiendo")
    
#el uso correcto sería el siguiente:
class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass
        
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):        
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print("El humano está comiendo")
        
    def dormir(self):
        print("El humano está durmiendo")
        
    def trabajar(self):
        print("El humano está trabajando")
    
class Robot(Trabajador):
    def trabajar(self):
        print("El robot está trabajando")
        
humano=Humano()
humano.trabajar()
humano.comer()
humano.dormir()
robot=Robot()
robot.trabajar()