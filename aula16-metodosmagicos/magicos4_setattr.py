"""
__setattr__ é um método que é acionado assim que você tenta atribuir algo fora da classe
que não existe dentro da classe.

Por exemplo, se tentar atribuir self.nome, mas não existe isso no __init__, o setattr irá
fazer esse trabalho por nós de atribur, MAS APENAS DENTRO DO __setattr__! Fora dele é como 
se esses atributos não existissem.

key = atributo
value = valor passado

Porém, é impossível acessar esses valores, a não ser que use o exemplo da classe B mais abaixo.
"""
print()

class A:
    def __init__(self):
        pass


    def __setattr__(self, key, value):
        print(key, value)  # nome Victor Martins


a = A()

a.nome = 'Victor Martins'
# print(a.nome)  # Descomentar isso aqui ocasiona em erro, pois não existe o atributo nome (somente dentro do setattr).


#################################################
print()
print("#"*20)
print()


class B:
    def __init__(self):
        pass


    def __setattr__(self, key, value):
        self.__dict__[key] = value  # Pra corrigir, colocamos o atributo dentro do "dicionário" da classe. Toda classe tem um dicionário oculto com todos os atributos criados.
        # Esse dicionário é acessado através do método __dict__, outro método mágico.


b = B()
b.nome = 'Victor Martins'
print(b.nome)  # Executado com sucesso.

# E com isso, posso usar __setattr__ para interceptar chaves e valores que serão passados. Não é uma boa prática de programação, mas é possível. Segue a Classe C.


#################################################
print()
print("#"*20)
print()


class C:
    def __init__(self):
        pass


    def __setattr__(self, key, value):
        if key == 'nome':  # Se o atributo tiver nome 'nome'...
            self.__dict__[key] = 'INTERCEPTADO!'  # ...manda essa string pra chave 'nome'.
        else:
            self.__dict__[key] = value  # Caso contrário, manda o valor recebido, que é 'Victor Martins'.


c = C()
c.nome = 'Victor Martins'
print(c.nome)

c.atributo_teste = 225
print(c.atributo_teste)  # Esse não foi interceptado pois a chave é 'atributo_teste', não 'nome'.
