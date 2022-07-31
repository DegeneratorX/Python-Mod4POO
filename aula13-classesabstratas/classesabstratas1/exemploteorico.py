"""
No primeiro exemplo de herança simples, foi mostrado a classe Pessoa, Cliente e Aluno.

A classe Pessoa é uma classe abstrata, pois ela é a mais genérica possível, e toda subclasse herda coisas dela. Ou seja, ela não tem nada de coisa exclusiva.

Classes abstratas: São classes que não precisam ser instanciadas. Geralmente são as classes mestre de tudo.
Podem ser instanciadas, mas não é uma boa prática de programação, afinal se ela é genérica, qualquer classe que herda seus atributos pode ser utilizada ao invés.

Para evitar essa má pratica de programação, utilizamos o módulo abc, que possui funções que irão basicamente nos "proibir" de instanciar a classe mestre.

Uma classe abstrata pode ter:
Métodos concretos
    São métodos normais, onde você escreve e ele funciona perfeitamente na herança ou na cadeia de herança.
Métodos abstratos
    São métodos que não tem corpo. Não escreve código nele, para que as outras classes filhas herdem este método e sejam OBRIGADAS a criar esse métodos nessas classes filhas.
"""
from abc import ABC, abstractmethod  # abstract base class (classe base abstrata) + decorador (igual os outros decoradores que usamos)

class A(ABC):  # Classe mestra. Recebe o parâmetro ABC do módulo abc
    @abstractmethod  # Usando isso aqui já é suficiente para impedir qualquer instância dessa classe.
    def falar(self):
        pass

# a = A() <- Instanciação imediata: isso acarreta em erro.
# Para resolver, criamos uma nova classe

class B(A):  # Herda tudo de A
    def falar(self):
        print('B está falando...')

obj = B()
obj.falar()
