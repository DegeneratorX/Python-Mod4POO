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
c1.comprar()
# c1.estudar() inexistente.

print()

a1 = Aluno('Luiz', 45)
print(a1.nome)
a1.falar()
a1.estudar()
# a1.comprar() inexistente.

print()

# Também posso vir e instanciar uma pessoa em si, não necessariamente cliente nem aluno.

p1 = Pessoa('André', 30)
p1.falar()
# p1.comprar() inexistente
# p1.estudar() inexistente.

# Como consequência, essa pessoa nem pode comprar nem pode estudar, pois a classe Pessoa não herda nada das subclasses.
