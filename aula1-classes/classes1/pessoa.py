"""
Função: função fora de uma classe
Método: função dentro de uma classe.

Self: por hora, esse parâmetro deve ser enviado de forma obrigatória nos métodos.
Quando estivermos falando de métodos estáticos, ai dá pra mudar.
Por hora, qualquer método criado deve ser passado o parâmetro 'self' primeiro.
O nome pode ser qualquer um, mas 'self' é por convenção o mais utilizado pela comunidade.
"""


class Pessoa:

    def falar(self):  # Self nada mais é do que o próprio objeto sendo passado.
        print('Pessoa está falando...')
# Toda vida que atribuir um método a um objeto, será 'self' como padrão.
