from Pessoa import *
from Usuario import *
class Funcionario(Pessoa, Usuario):
    def __init__(self, cpf, nome, pis ,senha,  ident = 0):
        Pessoa.__init__(self, cpf, nome, ident)
        Usuario.__init__(self, senha)
        self.pis = pis
    def getPis(self):
        return self.pis