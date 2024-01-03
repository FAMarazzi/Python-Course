#creando diccionarios con dict
diccionario= dict(nombre="lucas", apellido="dalto")

#las listas no pueden ser claves y
#podemos meter tuplas o cjtos con frozenset
diccionario= {
    frozenset(["dalto", "rancio"]): "jajaja"
    }

#creando diccionarios con fromkeys sin valores
#dato por defecto "None"
diccionario= dict.fromkeys(["nombre", "apellido"])

#creando diccionarios con fromkeys() con valor
#por defecto cambiado a "No se"
diccionario=dict.fromkeys(["nombre", "apellido"], "No se")

print (diccionario)