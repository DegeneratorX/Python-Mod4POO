"""
__init__: método que inicia uma classe. Ou seja, atribui valores padrões ao objeto (p1) instanciado (criado).
"""


class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):  # Método especial do python __init__.
        # Por padrão, deverá receber 'nome' e 'idade' obrigatoriamente.
        # 'comendo' e 'falando' estão setados 'False' por padrão.
        # Ou seja, não precisa passar 'comendo' e 'falando' no outro arquivo como parâmetro nesse método se não quiser.

        # Deve, ao usar __init__ e passar parâmetros, usar 'self.algo' e atribuir cada parâmetro respectivo passado.
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        # Isso é necessário para que os valores padrões passados sejam atribuídos ao objeto instanciado.
        # 'self' nada mais é que p1, p2, etc. nesse momento. p1.nome, p1.idade... igual no outro arquivo.

    def outro_metodo(self):
        print(self.nome)   # A variável com 'self' ficará disponível para todos os outros métodos, desde que ela esteja
        #                    declarada em __init__. Qualquer outra variável acarretará erro.

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return  # Usar return é FUNDAMENTAL para encerrar o método/função, ou ele executará tudo abaixo.
        if self.falando:
            print(f'{self.nome} já está falando.')
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:  # Se comendo == True
            print(f'{self.nome} já está comendo.')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False
