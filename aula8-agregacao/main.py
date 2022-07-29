"""
Agregação - um tipo de associação
Agregação: Uma classe usa outra classe mas ela precisa da outra classe
Exemplo: um carro precisa das rodas para funcionar. Eles existem, mas são muito dependentes.
onar.

Exemplo aqui no código:
Essa classe dos carrinhos pode funcionar sozinha, mas ela precisa dos produtos
Já a classe dos produtos não precisa em nada da classe do carrinho de compras.
"""
from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)  # Outro produto, mas com mesmos atributos

carrinho.lista_produto()
print(carrinho.soma_total())
