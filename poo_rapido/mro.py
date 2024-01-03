class A:
    def hablar(self):
        print("Hola desde A")
        
class F:
    def hablar(self):
        print("Hola desde F")
        
class B(A):
    def hablar(self):
        print("Hola desde B")
        
class C(F):
    def hablar(self):
        print("Hola desde C")
    
class D(B,C):
    def hablar(self):
        print("Hola desde D")
        
d=D()


#Funciona siendo primero el último hijo, luego se hereda al
#primer padre declarado y si tuviera padre, seguiría ese también.
#luego continúa con el segundo padre y el padre de su padre finalmente.
#lo de abajo imprime el orden de la herencia.
print(D.mro())

#podemos además llamar al método de una función no instanciada
#pero enviandole la instancia de un hijo para ejecutar esa
#en este caso hablaría desde F y no desde D como habitualmente
F.hablar(d)