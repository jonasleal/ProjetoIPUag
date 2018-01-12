class Pedido(object):
    
    def __init__(self, roupa, cliente, quantidade = 1, ident = 0):
        self.roupa = roupa
        self.cliente = cliente
        self.quantidade = quantidade
        self.ident = ident
    
    def getIdent(self):
        return self.ident
    
    def setIdent(self, ident):
        self.ident = ident
        
    def getCliente(self):
        return self.cliente
        
    def getRoupa(self):
        return self.roupa
        
    def getQuantidade(self):
        return self.quantidade
        