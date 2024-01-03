frase= input("Decí algo flaco, dale que te calculo cuánto vas a tardar en decirlo: ")
palabras_separadas= frase.split(" ")
cantidad_palabras= len(palabras_separadas)
print("-----------")
print(f'Dijiste {cantidad_palabras} palabras, y tardarías {cantidad_palabras/2} segundos en decirlas')
print("-----------")
print(f'Igual de paso te aviso que dalto tardaría {cantidad_palabras/2*0.7} segundos en decir la gran pelotudez que dijiste vos lol')
print("-----------")
if(cantidad_palabras>120):
    print(f'Igual banca flaco, tampoco te pedí un testamento boludín')
    print("-----------")
    
