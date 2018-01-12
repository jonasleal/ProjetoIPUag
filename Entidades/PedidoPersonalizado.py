from Entidades.Pedido import *
class PedidoPersonalizado(Pedido):
    
    def __init__(self, roupa, cliente, quantidade = 1, medidas, observacoes = "", ident = 0):
        Pedido.__init__(self, roupa, cliente, quantidade, ident)
        self.medidas = medidas 
        self.observacoes = observacoes
    
    def getObservacoes(self):
        return self.ident
        
    def getMedidas(self):
        return self.cliente