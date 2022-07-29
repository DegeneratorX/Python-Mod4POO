"""Veja que oS códigos abaixo são idênticos. Evitar repetições na prog. é fundamental.

 class Aluno:
     def __init__(self, nome, idade):
         self.nome = nome
         self.idade = idade

 class Cliente:
     def __init__(self, nome, idade):
         self.nome = nome
         self.idade = idade

Herança entra pra eliminar repetições de código e fazer "tipos de tipos" de classes.

Afinal, clientes e alunos são pessoas.
"""

class Pessoa:  # Superclasse
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__  # Atributos especiais que mostram, pela instância, que tipo de "subclasse" está sendo executada, se é alunos ou clientes.
    
    def falar(self):
        print(f"{self.nomeclasse} está falando...")


class Cliente(Pessoa):  # Subclasse
    pass


class Aluno(Pessoa):
    pass
