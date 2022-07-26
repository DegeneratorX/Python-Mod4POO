class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramentas = None

    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramentas

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramentas = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever_caneta(self):
        print("Caneta está escrevendo...")


class MaquinaDeEscrever:
    def escrever_maquina(self):
        print("Máquina está escrevendo...")
