#import modulo_saludar as m_saludar

#saludo=m_saludar.saludar("Gabi")

#desde ese modulo importo 2 funciones
#y les asigno un nombre para usarlas
from modulo_saludar import saludar as saludar_normal,saludar_como_boludo as saludar_raro

#creamos las variables y no hay que
#nombrar el módulo
saludo=saludar_normal("Luqui")
saludo_raro=saludar_raro("Putin tontin")

#saludar
print(saludo)
print(saludo_raro)

#podemos ver las props y metodos del namescpace
#print(dir(m_saludar))

#accedo al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo
#print(m_saludar.__name__)