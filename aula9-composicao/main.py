"""
Composição: é a relação mais forte entre classes
Uma classe vai ser dona do objeto de outras classes
"""

from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()
# del cliente1

# DESCOMENTAR PARA ENTENDER: Se descomentar os 'del', perceberá que eu irei deletar apenas o objeto clientes1, e o endereço IRÁ JUNTO! Fazendo o trab. do garbage collector.
# Isso é composição. Quando deleta uma instância, a outra classe (endereço) morre junta. Uma realmente depende fortemente da outra pra sequer existir.

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
print()
# del cliente2

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
# del cliente3

print('#'*30)

print("TUDO EXECUTADO AQUI PRA BAIXO É PEGO PELO GARBAGE COLLECTOR E DELETADO DA MEMÓRIA EM SEGUIDA")
