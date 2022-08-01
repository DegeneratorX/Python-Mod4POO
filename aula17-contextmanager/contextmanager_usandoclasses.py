"""
Ao invés de usar "open()", uso uma classe pra abrir e fechar arquivos.

Exemplo abaixo, ao invés de 'with open()', uso 'with Arquivo()', e assim consigo manipular o arquivo dentro de uma classe.
"""


class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):  # Obrigatório quando a classe recebe arquivo.
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):  # Obrigatório quando a classe recebe arquivo. Esses parâmetros 'exc' são possíveis exceções levantadas que o método pode receber.
        print('fechando arquivo')
        self.arquivo.close()

        return True

with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')
