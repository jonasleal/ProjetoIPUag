from datetime import *
class Compra(object):
    def __init__(self, pedidos = [], data = datetime.now(), ident = 0):
        self.ident = int(ident)
        self.pedidos = pedidos
        self.data = data
        
        
    def getData(self):
        return self.data
    
    def getPedidos(self):
        return self.pedidos
    
    def getValor(self):
        saida = 0.0
        for pedido in self.pedidos:
            saida += float(pedido.getValor())
        return saida 
    
    def getIdent(self):
        return self.ident
    
    def setIdent(self, ident):
        self.ident = ident
    
    def addPedido(self, p):
        self.pedidos.append(p)
        
    def __str__(self):
        pedidos = "["
        for i in self.pedidos:
            pedidos+= str(i.getIdent()) + ','
        pedidos += "]"
        
        return "\nCompra \n" + "ID : " + str(self.ident) + pedidos + "Data : " + str(self.data)