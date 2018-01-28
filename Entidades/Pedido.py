class Pedido(object):
    
    def __init__(self, roupa, cliente, funcionario, quantidade = 1, ident = 0):
        self.roupa = roupa
        self.cliente = cliente
        self.funcionario = funcionario
        self.quantidade = int(quantidade)
        self.ident = int(ident)
    
    def getIdent(self):
        return self.ident
    
    def setIdent(self, ident):
        self.ident = int(ident)
        
    def getValor(self):
        saida = (self.roupa.getPreco() * self.quantidade)
        return saida
        
    def getCliente(self):
        return self.cliente
        
    def getRoupa(self):
        return self.roupa
        
    def getQuantidade(self):
        return self.quantidade
    def getFuncionario(self):
        return self.funcionario
    
    def __str__(self):
        saida = "\nPedido \n"
        saida += "ID : " + str(self.ident)
        saida += "\nCliente : " + str(self.cliente.getIdent())
        saida += "\nFuncionario : " + str(self.funcionario.getIdent())
        saida += "\nQuantidade : " + str(self.quantidade)
        saida += "\nRoupa : " + str(self.roupa.getID())+ "\n"
        return saida
        