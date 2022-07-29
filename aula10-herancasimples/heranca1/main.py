"""
Associação - Usa
Agregação - Tem
Composição - É dono
Herança - É outro objeto
"""

from classes import *

c1 = Cliente('Victor', 25)
print(c1.nome)
c1.falar()


a1 = Aluno('Luiz', 45)
print(a1.nome)
a1.falar()
