from Entidades.Pessoa import *
class Usuario(Pessoa):
    def __init__(self, cpf , senha, nome = "", ident = 0):
        Pessoa.__init__(self, cpf, nome, ident)
        self.senha = senha
        
    def getSenha(self):
        return self.senha