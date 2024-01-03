#El principio OCP dice que un programa
#debe estar abierto a agregar nuevas funcionalidades
#y cerrado a modificaciones.
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario=usuario
        self.mensaje=mensaje
        
    def notificar(self):
        #obligo a que se implemente en las clases hijas
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por correo electrónico a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.celular}")

#de esta forma cree un notificador que está cerrado a modificaciones
# y permite añadir nuevas funcionalidades
#por ejemplo podría añadir notificador por mensaje
#de instagram