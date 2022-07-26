"""
Encapsulamento:
Serve para esconder certas partes do seu código
pra proteger a sua aplicação, a sua classe, atributo ou método.

public, protected, private

public    - são métodos e atributos que podem ser acessados dentro e fora da classe
protected - são métodos e atributos que podem ser acessados somente dentro da classe ou das filhas daquela classe.
private   - são métodos e atributos que podem ser acessados somente dentro da classe.

_ private (fraco) (protected)
__ private (forte)

"""

class BaseDeDados:
    def __init__(self):
        self.dados = {}  # Crio uma base de dados vazia

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:  # Lembrando que não precisa adicionar .keys(). O python já entende que se não colocar, é por chave que se busca.
            self.dados['clientes'] = {id:nome}  # Se não tiver nada, é criado um dicionário
        else:
            self.dados['clientes'].update({id:nome})  # Se tiver, atualiza o valor da chave. .update lembrando, é uma função de dicionários (rever).

    def lista_clientes(self):  # Printa todos os clientes do dicionário
        for id, nome in self.dados['clientes'].items():  # Desempacotamento
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]  # Acesso a chave 'clientes', e do valor acessado, acesso a chave 'id' e deleto o valor.

bd = BaseDeDados()

print()
bd.inserir_cliente(1, 'Victor')  # Insiro 3 clientes
bd.inserir_cliente(2, 'Fernando')
bd.inserir_cliente(3, 'Maria')
print(bd.dados)

print()

bd.apaga_cliente(2)  # Apago 'Fernando'
bd.lista_clientes()

bd.dados = 'String pra dar erro em toda a classe!'
#############
# bd.lista_clientes()  # Isso ocasionará erro, basta descomentar e verá.

# Pois estou atribuindo a self.dados uma string, e os métodos que trabalham com self.dados trabalham com dicionário, e não string.
# Solução no próximo arquivo.
#############