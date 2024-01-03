#Single Responsability Principle
#Principio de Responsabilidad Única
#Este principio dice que cada clase que creemos
#debe encargarse de una sola o pocas responsabilidades
#acordes a lo que creamos
class Auto():
    def __init__(self, tanque):
        self.posicion=0
        self.tanque=tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion+=distancia
            self.tanque.usar_combustible(distancia/2)
        else:
            print("No hay suficiente combustible para recorrer esa distancia")

class TanqueDeCombustible():
    def __init__(self):
        self.combustible=100
    
    def agregar_combustible(self,cantidad):
        self.combustible+=cantidad
        
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible -=cantidad
        
tanque=TanqueDeCombustible()
autito=Auto(tanque)

autito.mover(20)
combustible=autito.tanque.obtener_combustible()
print(combustible)
autito.mover(120)
combustible=autito.tanque.obtener_combustible()
print(combustible)
    