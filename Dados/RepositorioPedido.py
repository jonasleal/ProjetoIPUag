class RepositorioPedido(object):
    def __init__(self, dados):
        self.dados = dados
    
    def salvar(self, pedido):
        return self.dados.salvar(pedido)
    
    def buscarPorCliente(self, cliente):
        return self.dados.salvar(cliente)
    
    def recuperar(self, ident):
        return self.dados.recuperar(ident)