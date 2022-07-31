"""
Sobreposição de métodos:
Criação de um método dentro de uma subclasse com o mesmo nome que sobrepõe todos os valores do método original da classe mestre. 
"""

from classes import *

c1 = Cliente('Luiz', 23)  # Perceba que com herança, __init__ vale para todas as classes, incluindo "Cliente"
c1.comprar()

print()

c2 = clienteVIP('Victor', 25)
c2.falar()  # Ele primeiro procura o método no ClienteVIP, depois procura na classe Cliente, e finalmente na classe Pessoa.
# Se eu crio um método 'def falar(self):' na classe ClienteVIP, estarei sobrepondo o método original da classe Pessoa.
# Isso é a sobreposição (de métodos)

# Irei abordar isso na próxima pasta.
