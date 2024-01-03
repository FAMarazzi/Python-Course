

cadena1= "Hola,soy,Fedu"
cadena2="Que onda bro?"

#se puede usar dir para ver todos los atributos
#de algo en python. Ejemplo:
atributos_cadena1=dir(cadena1)
# print(atributos_cadena1) devolvería todos los atributos de una cadena.

#convierte a mayúsculas
mayusc= cadena1.upper() #(metodo)

#convierte a minúsculas
minusc= cadena1.lower()

#primer letra mayúscula y resto en minúsculas
primer_letra_mayusc=cadena1.capitalize()

#busca una cadena dentro de otra cadena.
#si la encuentra devuelve la posición
#si no la encuentra devuelve -1

busqueda_find= cadena1.find("F")

#busca una cadena dentro de otra
#todo igual pero si no la encuentra lanza una excepción

busqueda_index= cadena1.index("u")

#si es numérico devuelve True

es_numerico= cadena1.isnumeric()

#si es alfanumérico devuelve True
#para ser alfanumerico solo debe tener letras de la A-Z
#y no debe tener ni numeros ni caracteres ni espacios...

es_alfanumerico= cadena1.isalpha()


#cuenta las coincidencias de una cadena dentro de otra cadena
# y devuelve esa cantidad.

contar_coincidencias= cadena1.count("o")

#cuenta los caracteres de una cadena
#este no es un metodo, es una función

contar_caracteres = len(cadena1)

#verifica si una cadena empieza con otra cadena dada
#si es correcto, devuelve True

empieza_con= cadena1.startswith("H")

#verifica si una cadena termina con otra cadena especifica
#si es asi, devuelve True

termina_con= cadena1.endswith("edu")

#busca el primer valor dado en la cadena original, y lo reemplaza por el segundo
#si no lo encuentra, deja igual la cadena original.

cadena_modificada= cadena1.replace("Fedu", "Carla")

#separa cadenas con la cadena que pasemos, y devuelve una lista de las cadenas separadas.

cadena_separada=cadena1.split(",")

print(cadena_separada)