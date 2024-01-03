#usando open para abrir un archivo con una codificación universal
archivo = open("archivos\\texto_fedu.txt", encoding="UTF-8")

#leer archivo
#texto_leido=archivo.read()

#leer una sola linea
#linea=archivo.readline()

#leer linea por linea y guardar en una lista
lineas=archivo.readlines()

#cerrar archivo
archivo.close()
print(lineas)