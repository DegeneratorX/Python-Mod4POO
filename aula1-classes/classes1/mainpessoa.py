"""
Instância de um objeto/classe - Criação de um objeto a partir de uma classe
"""

from pessoa import Pessoa
# Importação de classe

p1 = Pessoa()
p2 = Pessoa()
# p1 != p2
# Quando se instancia (copia) uma classe para um objeto (p1, p2), sempre serão atribuídos valores diferentes ao chamar,
# pois apontarão para diferentes lugares da memória.
print(p1) # Prova disso.
print(p2)
# Ou seja, estamos utilizando um molde para criar uma pessoa p1, e outro molde para criar uma pessoa p2 completamente
# diferente. Sempre que chama essas clases, será automaticamente setado como se fossem pessoas diferentes.

# Para chamar métodos, é igual chamar função normal.
# Primeiro põe o objeto, depois o método.
p1.falar()  # implicitamente tem self. Isso é explicado no outro arquivo.
# Mas basicamente é como se fosse p1.falar(p1). Só não é exatamente isso pq no caso seria atribuição 2 vezes.
# E não seria falar(p1) apenas, pq a função falar não está definida nessa main, e sim em outro arquivo.
