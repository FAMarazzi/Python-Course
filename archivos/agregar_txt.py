#abro archivo con permiso append "a" para agregar texto
with open("archivos\\texto_fedu.txt", 'a', encoding="UTF-8") as archivo:
    #agrega la linea al texto ya escrito
    
    archivo.write("Agregando texto\n")
    
    #uso un for para agregar lineas
    for i in range(5):
        archivo.write(f'Esta es la línea {i+1} agregada \n')
  