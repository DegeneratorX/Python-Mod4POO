"""
->
Ao final de todo método ou função, você indica para eles o que tem que retornar.
Caso retorne outra coisa, o código funciona, mas a IDE irá reclamar.
"""


def funcao(p1: float, p2: str, p3: dict) -> float:  # Essa função precisa retornar float.
    return 10.10


print(funcao(10.1, 'frase', {}))


##########################################
print()
print("#"*20)
print()

# Para que você escolha múltiplos tipos que podem retornar, se usa Union.

from typing import Union


def funcao2() -> Union[list, dict]:  # Deve retornar lista ou dict.
    return []
