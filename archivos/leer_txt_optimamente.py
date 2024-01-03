
with open("archivos\\texto_fedu.txt", encoding="UTF-8") as archivo:
    #leemos archivo
    contenido=archivo.read()
    
    #mostramos archivo
    print(contenido)

#no es necesario cerrarlo con with open.
#ya que todo lo que se haga dentro es con archivo abierto