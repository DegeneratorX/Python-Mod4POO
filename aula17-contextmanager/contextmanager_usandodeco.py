"""
Existe a opção de uso de decorador. É menos linha de código e mais utilizado.
Usa apenas função.
"""

from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)  # Guardo o arquivo numa variável criada aqui
        yield arquivo  # Retorno o arquivo com yield. Se fosse 'return', não executaria nada abaixo disso. Ou seja, o arquivo não seria fechado.
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
