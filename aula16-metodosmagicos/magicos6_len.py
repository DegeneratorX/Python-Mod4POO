"""
__len__ é muito útil quando for contar os objetos dentro de uma classe, assim
quando chamar a função len(objeto), ele retornará o que vier em __len__.

Sem __len__, usar o len() no objeto ocasionará em error.
"""


class A:
    def __init__(self):
        pass


    def __len__(self):
        return 55


a = A()
print(len(a))
