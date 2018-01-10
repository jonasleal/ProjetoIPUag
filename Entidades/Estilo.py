class Estilo(object):
    def __init__(self,nome , ident = 0):
        self.nome = nome
        self.ident = ident
        
    def getNome(self):
        return self.nome
    
    def getIdent(self):
        return self.ident
    
    def setIdent(self, ident):
        self.indet = ident
    
    def __str__(self):
        return self.nome