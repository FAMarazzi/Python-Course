diccionario={
    "nombre": 'Fede',
    "apellido": 'Marazzi',
    "dni": 12345678
}

#devuelve un objeto dict_item con los keysS
claves = diccionario.keys()

#devuelve un elemento enviandole su key con get
#en lugar de usar diccionario["nombre"] ya que detiene el programa
#con get no devuelve una excepcion si no se encuentra, y devuelve None

valor_kaskas= diccionario.get("kaskas")

#elimina el diccionario
#LO COMENTO PARA QUE NO BORRE TODOS LOS ELEMENTOS

#diccionario.clear()


#elimina un "atributo" del diccionario

diccionario.pop("dni")


print(diccionario)