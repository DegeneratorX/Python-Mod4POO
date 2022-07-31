class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    def falar(self):
        print(f'{self.nomeclasse} está falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')
    
    def falar(self):
        print('Estou em CLIENTE.')


class clienteVIP(Cliente): 
    def falar(self):
        super().falar()  # super(): pega o método anterior na hierarquia, em seguida o nome do método para execução
        Pessoa.falar(self)  # Alternativa: ser específico quanto a classe e executar o método. Passar parâmetros como 'self' são obrigatórios nesse caso.
        Cliente.falar(self)
        print('Estou em clienteVIP')
