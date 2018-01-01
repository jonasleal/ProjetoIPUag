from Pessoa import *
from Usuario import *
class Cliente(Pessoa, Usuario):
    def __init__(self, cpf, nome, senha, ident = 0):
        Pessoa.__init__(self, cpf, nome, ident)
        Usuario.__init__(self, senha)
    