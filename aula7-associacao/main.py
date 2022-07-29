"""
Associação: uma classe utiliza outra classe, e uma pode viver sem a outra também.

Existem dois subtipos de associação:
Agregação (aula 8)
Composição (aula 9)

Nessa aula 7 será abordado somente uma explicação genérica de associação.
"""

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta  # Associação: quando eu jogo um objeto (classe) inteiro pra uma variável de outra classe
escritor.ferramenta.escrever_caneta()  # E assim posso chamar um método de outra classe fora dessa classe.

escritor.ferramenta = maquina
escritor.ferramenta.escrever_maquina()
