"""
Getters e Setters são extremamente úteis para puxar valores, fazer alterações neles
e não alterar as linhas de códigos originais.
Ou seja, acrescento mais linha de código, mas não mexo no que já existe.

No exemplo abaixo, estou pegando o preço e tirando o R$ e convertendo o resto em float, sem alterar o método "desconto()".
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))


    # Getter
    @property  # Obrigatório para definir um get
    def preco(self): # Pego o atributo que desejo alterar, no caso o método leva o mesmo nome do atributo
        return self._preco  # Retorno '_atributo'. Por convenção se usa '_' antes do nome em si, mas poderia ser qualquer coisa. A ideia é não haver conflito com o 'preco' original.

    # Setter
    @preco.setter  # Obrigatório pra definir um set
    def preco(self, valor):  # Defino o nome do método sendo o mesmo do atributo novamente, dessa vez passo valores que desejo alterar
        if isinstance(valor, str):  # isinstance() retorna bool ao checar se o objeto passado pertence (é instanciado) a uma classe específica, no caso aqui verifica se é class string.
            valor = float(valor.replace('R$', ''))  # Se sim, tira o cifrão.
        self._preco = valor  # Atualiza o valor do preço


p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', 'R$15')  # No caso de receber uma string ao invés de int ou float, daria erro.
p2.desconto(10)
print(p2.preco)
