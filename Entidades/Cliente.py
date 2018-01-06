from Usuario import *
class Cliente(Usuario):
    def __init__(self, cpf, nome, senha, ident = 0):
        Usuario.__init__(self, cpf , senha, nome, ident )
    