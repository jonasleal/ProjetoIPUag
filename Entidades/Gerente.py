from Funcionario import *
class Gerente(Funcionario):
    def __init__(self, cpf, nome, pis , senha, ident = 0):
        super(Gerente, self).__init__(cpf, nome, pis , senha, ident)
    