from distutils.log import error


"""
Criação de exceção
"""

class ExplosionError(Exception):  # Sim, são duas linhas de código apenas. A classe do erro novo herda a classe Exception, uma classe built-in.
    pass

def explosao():
    raise ExplosionError("Your code has been exploded by unknown enemies.")

try:
    explosao()
except ExplosionError as errobrabo:
    print(f'Erro: {errobrabo}')  # Criei, levantei e tratei minha própria exceção.
