from Usuario import *
class Funcionario(Usuario):
    def __init__(self, cpf, nome, senha, pis,  ident = 0):
        Usuario.__init__(self, cpf , senha, nome, ident)
        self.pis = pis
    def getPis(self):
        return self.pis