class Celular:
    #creamos el constructor (debe recibir self siempre)
    def __init__(self, marca, modelo, camara):
        self.marca=marca
        self.modelo=modelo
        self.camara=camara
    #todo metodo debe recibir el self para ser un metodo de objeto
    def llamar(self):
        print(f"Llamando desde el {self.modelo}...")
    
    def cortar(self):
        print(f"Colgando llamada desde el {self.modelo}")

celular1=Celular("Samsung", "S22 FE Edition", "48MP")
celular2=Celular("Apple", "Iphone 9", "28MP")
celular2.llamar()
celular1.cortar()