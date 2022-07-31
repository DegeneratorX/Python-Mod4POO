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
    def __init__(self, nome, idade, sobrenome):  # Sobreposição de construtores também pode ocorrer. Por exemplo, se o clienteVIP precisar de um sobrenome adicional para o cadastro.
        super().__init__(nome,idade)  # OBRIGATÓRIO! 
        # Pessoa.__init__(self, nome, idade)  # Também funciona!

        self.sobrenome = sobrenome  # Criação de um atributo da classe clienteVIP apenas.
    
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome} está falando...')
