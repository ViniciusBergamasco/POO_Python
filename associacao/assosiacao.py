from classes import Escritor
from classes import Caneta
from classes import MaquinaEscrever

escritor = Escritor("João")
print(escritor.nome)

caneta = Caneta("Bic")
print(caneta.marca)

maquina = MaquinaEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()