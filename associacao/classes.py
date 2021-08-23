class Escritor:
    def __init__(self,nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self.__ferramenta = ferramenta
    
    @property
    def nome(self):
        return self.__nome

class Caneta:
    def __init__(self,marca):
        self.__marca = marca

    def escrever(self):
        print("Caneta está escrevendo...")

    @property
    def marca(self):
        return self.__marca

class MaquinaEscrever:
    def escrever(self):
        print("Máquina está escrevendo...")