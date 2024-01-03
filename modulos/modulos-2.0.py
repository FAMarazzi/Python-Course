#si el módulon estuviera en una carpeta
#en la misma ruta  sería
#import funciones_buenas.saludar as m_saludar

#print(m_saludar.saludar("Bro"))

import sys

sys.path.append('D:\\Fedu\\Escritorio\\CURSO PYTHON\\funciones_buenas')
import saludar as m_saludo
print(m_saludo.saludar("Fede"))
