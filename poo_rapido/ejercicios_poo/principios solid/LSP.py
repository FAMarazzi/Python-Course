#Principio de Sustitución de Liskovs
#Una clase hija deebe poder hacer todo
#lo que hace la clase padre y mas
#no puede deshacer algo del padre

# class Ave:
#     def volar(self):
#         return "Estoy volando"

# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"

#esto estaría mal. para corregirlo deberíamos
#hacer lo siguiente

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"

class AveNoVoladora(Ave):
    pass

avenovoladora=AveNoVoladora()