"""
__str__ é um método bem simples.

Sempre que tentar printar a instância em si, mostrará apenas o objeto, sua classe e endereço.
Mas ao usar o '__str__', ele ativa e entra em ação automaticament, e o print() mostrará o que retornar no __str__.
"""


class A:
    def __init__(self):
        pass


    # def __str__(self):
    #     return "<class 'A'>"


a = A()
print(a)


#####################################
print()
print("#"*20)
print()


class B:
    def __init__(self):
        pass


    def __str__(self):
        return "<class 'B'>"


b = B()
print(b)