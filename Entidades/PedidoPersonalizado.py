from Entidades.Pedido import *
class PedidoPersonalizado(Pedido):
    
    def __init__(self, pedido, medidas, observacoes = ""):
        Pedido.__init__(self, pedido.getRoupa(), pedido.getCliente(), pedido.getFuncionario(), pedido.getQuantidade(), pedido.getIdent())
        self.medidas = medidas 
        self.observacoes = observacoes
    
    def getObservacoes(self):
        return self.ident
        
    def getMedidas(self):
        return self.cliente