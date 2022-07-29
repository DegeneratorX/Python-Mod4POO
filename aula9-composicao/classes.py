class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []  # Recebe objetos da classe Endereço


    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))  # Chamando a classe Endereco(). Meio que "instanciando"


    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        # Tudo aqui é visual e apenas pra mostrar como os objetos estão sendo deletados
        print(f'{self.nome} foi APAGADO!')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    