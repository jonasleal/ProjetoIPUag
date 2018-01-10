class Pessoa(object):
    def __init__(self, cpf, nome, ident = 0):
        self.ident = int(ident)
        self.nome = nome
        self.cpf = cpf
    def getIdent(self):
        return self.ident
    def setIdent(self, ident):
        self.ident = int(ident)
    def getNome(self):
        return self.nome
    
    def getPrimeiroNome(self):
        primeiroNome = self.nome.split(" ")
        
        if len(primeiroNome) > 0:
            primeiroNome = primeiroNome[0]
        return primeiroNome
    
    def getCpf(self):
        return self.cpf
    def __str__(self):
        return self.nome
    