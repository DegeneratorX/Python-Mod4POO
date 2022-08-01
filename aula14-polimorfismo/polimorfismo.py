"""
Polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (de mesma assinatura),
mas comportamentos diferentes.

Mesma assinatura = Mesma quantidade e tipo de parâmetros

OBS: Usamos polimorfismo na aula anterior, com contas. Basicamente TODOS os métodos abstratos geram polimorfismo, pois o
programador é obrigado a criar métodos em outras classes que precisam ser definidos com o mesmo nome do método abstrado
da superclasse.
"""

from abc import ABC as abstractclass
from abc import abstractmethod

class A(abstractclass):
    @abstractmethod
    def fala(self, msg): pass

class B(A):
    def fala(self, msg):  # Sou obrigado a criar esse método para definir comportamento diferente pra cada subclasse. Isso é polimorfismo.
        print(f'B está falando {msg}')
class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()

b.fala('Um assunto')
c.fala('Outro assunto')