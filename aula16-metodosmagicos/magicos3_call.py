"""
O método __call__ faz nossa classe se comportar como uma função.
"""


class A:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)


a = A()
a(1, 2, 3, 4, 5, nome='Victor')


############################################
print()
print("#"*20)
print()


class B:
    def __init__(self):
        pass

    
    def __call__(self, *args, **kwargs):
        resultado = 1

    
        for i in args:
            resultado *= i

        return resultado

    
    def fala_oi(self):
        print('Oi')


b = B()
variavel = b(1,2,3,4,5,6,7,8)  # Quando uso a instância como função, automaticamente cai no método __call__.
b.fala_oi()  # E não deixa de ser uma instânciação de classe, b.fala_oi() é a prova disso.
print(variavel)