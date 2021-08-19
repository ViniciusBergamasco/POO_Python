"""
Encapsulamento em linguagens "clássicas":
public,protected,private

Convenções em Python:
"_" protected(public _)
"__" privado (_NOMECLASSE__NOMEATRIBUTO)
"""

class BaseDeDados:
    def __init__(self,):
        self._dados = {}

    def inserir_cliente(self,id,nome):
        if 'clientes' not in self._dados:
            self._dados['clietes'] = {id: nome}
        else:
            self._dados['clientes'].update({id:nome})
    
    def listar_clientes(self):
        for nome,id in self._dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self,id):
        del self._dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1,'Vinicius')
bd.inserir_cliente(2,'Maria')
bd.listar_clientes()