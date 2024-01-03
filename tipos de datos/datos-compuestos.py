#declaración lista (se puede modificar)

lista=["Fede", "fedd", True, 1.79] 

#declaración tupla (no se puede modificar)

tupla=("Fede", "fedd", True, 1.79)

#esto es válido
lista[3]="Crack"

#esto no
#tupla[3]="Crack"

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados, sus elementos no están ordenados)

conjunto= {"Fede", "fedd", True, 1.78, "Fede"}

#print (conjunto[3]) -> No puede acceder al elemento


#creando un diccionario (dict) (la estructura es key: value y separamos por comas)
diccionario={
    'nombre': "Fede",
    'nombre_artistico': "fedd",
    'esta_feliz': True,
    'altura': 1.78
}

print (diccionario['altura'])

