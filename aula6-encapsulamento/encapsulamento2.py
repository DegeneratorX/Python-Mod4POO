"""
Encapsulamento:
Serve para esconder certas partes do seu código
pra proteger a sua aplicação, a sua classe, atributo ou método.
Inclui proteger para que devs não alterem essa parte do código em específico na classe,
pois se alterar pode ocorrer erros em cascata.

public, protected, private

public    - são métodos e atributos que podem ser acessados dentro e fora da classe
protected - são métodos e atributos que podem ser acessados somente dentro da classe ou das filhas daquela classe.
private   - são métodos e atributos que podem ser acessados somente dentro da classe.

_ private (fraco) (protected)
__ private (forte)

"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()

print()
bd.inserir_cliente(1, 'Victor')  # Insiro 3 clientes
bd.inserir_cliente(2, 'Fernando')
bd.inserir_cliente(3, 'Maria')

print()

bd.apaga_cliente(2)  # Apago 'Fernando'

bd.__dados = 'String pra dar erro em toda a classe!'
print(bd.__dados)

bd.lista_clientes()  # Agora não dará mais erro, pois dei refactor em 'dados' e adicionei __ antes dele,
# assim todos os 'dados' do código ficaram __dados, e assim o atributo se tornou private.
# Não é possível acessar facilmente ele. Quando se usou bd.__dados fora da classe, na verdade ele criou uma variável do zero
# e jogou a string lá.

# Agora pra acessar os dados private, é necessário fazer isso aqui:
print()
print("Aqui está o dicionário privado acessado: ", bd._BaseDeDados__dados)
