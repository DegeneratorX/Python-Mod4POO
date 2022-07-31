class Eletronico:  # Eletrônico genérico
    def __init__(self, nome):  # Construtor de um eletrônico
        self._nome = nome
        self._ligado = False  # Por padrão, desligado

    def ligar(self):
        if self._ligado:  # Se já estiver ligado, não retorna nada, tá sussa.
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:  # Se já estiver desligado, não retorna nada, tá sussa.
            return
        self._ligado = False
