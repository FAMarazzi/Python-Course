#importo expresiones regulares
import re

#defino un texto
texto='''Hola maestro, esta es la cadena 1. Como estás papá
Esta es la línea 2 del texto.
Y esta es la línea final( la 3.000 ) definitiva papá'''

#hago una búsqueda simple
resultado= re.findall("Esta", texto)

#\d -> busca digitos numéricos del 0-9
resultado= re.findall(r"\d", texto)          #el r es como el f, solo que indica que vamos a usar expresiones regulares

#\D -> busca TODO menos digitos numéricos del 0-9 (las MAYUS suelen hacer lo contrario)
resultado= re.findall(r"\D", texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado= re.findall(r"\w", texto)   

#\w -> busca TODO menos caracteres alfanumericos [a-z A-Z 0-9 _]
resultado= re.findall(r"\W", texto)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
resultado= re.findall(r"\s", texto)   

#\S -> busca TODO menos espacios en blanco
resultado= re.findall(r"\S", texto)

#. -> Busca TODO menos saltos de linea
resultado =re.findall(r".", texto)

#\n -> Busca saltos de linea
resultado =re.findall(r"\n", texto) 
 
#\ Poniendo una barra antes cancela expresiones regulares, cancelando la función del punto para buscar puntos 
resultado=re.findall(r"\.", texto)

#armo cadena que busque numero seguido de punto seguido de espacio
resultado=re.findall(r"\d\.\s", texto)

#^ -> busca el comienzo de línea(Buscando hola al principio de la linea)
#usar flags=re.M activa la multilinea. Si no estuviera, buscaría solo en la primer linea
resultado= re.findall(r"^Esta", texto, flags=re.M)

#$ -> busca el finañ de línea(Buscando papá al final de la linea)
resultado= re.findall(r"papá$", texto, flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izq (3 numeros juntos)
resultado=re.findall(r"\d{3}", texto)

#{n,m} -> al menos n, como máximo m (al menos 1 numero, máximo 4)
resultado=re.findall(r"\d{1,4}", texto)

# | -> Busca una cosa u otra (Devuelve cadenas de 1 numero minimo, 4 maximo, o Hola)
resultado=re.findall(r"\d{1,4}|Hola", texto)
print(resultado)