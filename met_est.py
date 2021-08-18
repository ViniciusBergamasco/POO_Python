from random import randint
from datetime import datetime

class Pessoa:

    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) 
    def __init__(self,nome,idade,comendo=False,falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    #Metodo estático
    @staticmethod
    def gera_id():
        rand = randint(10000,99999)
        return rand

print(Pessoa.gera_id())