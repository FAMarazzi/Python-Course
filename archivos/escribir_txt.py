#abro con permiso w de escritura
with open("archivos\\texto_fedu.txt", 'w', encoding="UTF-8") as archivo:
    #SOBRESCRIBE EL ARCHIVO
    archivo.write("LE MOULIN\n")
    
    #agrego 2 líneas con write lines
    archivo.writelines(["Agregando primera línea \n", "Agregando segunda línea\n"])
    
    #agrego otras 2 lineas
    archivo.writelines(['Agregando tercera línea \n', 'Agregando cuarta línea\n'])
    