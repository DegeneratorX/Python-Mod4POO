from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):  # Smartphone herda atributos do Eletrônico, afinal ele é um eletrônico. E herda LogMixin, pois tenho intenção de gerar log de erros ou informações.
    def __init__(self, nome):  # Construtor próprio com atributos exclusivos
        super().__init__(nome)  # Herda o construtor da classe mãe, afinal não queremos que haja um "conflito" de métodos (sobreposição)
        self._conectado = False  # Por padrão, o smartphone não está conectado à internet.

    def conetar(self):
        if not self._ligado:
            error = f'{self._nome} NÃO ESTÁ LIGADO, PORTANTO NÃO TEM COMO CONECTAR'  # Guardo a string numa variável, pois irei usar a variável múltiplas vezes.
            print(error)
            self.log_error(error)  # 
            return

        if self._conectado:
            error = f'{self._nome} JÁ ESTÁ CONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi conectado com sucesso!.'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} JÁ ESTÁ DESCONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desconectado com sucesso!.'
        print(info)
        self.log_info(info)
        self._conectado = False
