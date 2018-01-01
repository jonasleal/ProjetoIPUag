class Pessoa(object):
    def __init__(self, cpf, nome, ident = 0):
        self.ident = ident
        self.nome = nome
        self.cpf = cpf
    def getIdent(self):
        return self.ident
    def setIdent(self, ident):
        self.ident = ident
    def getNome(self):
        return self.nome
    def getCpf(self):
        return self.cpf
    def __str__(self):
        return self.nome
    