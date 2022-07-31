"""
Sobreposição de métodos:
Criação de um método dentro de uma subclasse com o mesmo nome que sobrepõe todos os valores do método original da classe mestre. 
"""

from classes import *

c1 = Cliente('Luiz', 23)
c1.comprar()

print()

c2 = clienteVIP('Victor', 25)
c2.falar()
