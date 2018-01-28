class RepositorioCompra(object):
    def __init__(self, dados):
        self.dados = dados
    
    def salvar(self, pedido):
        return self.dados.salvar(pedido)
    
    def buscarPorCliente(self, cliente):
        return self.dados.salvar(cliente)
    
    def recuperarPorPeriodo(self, dataInicial, dataFinal):
        return self.dados.recuperarPorPeriodo(dataInicial, dataFinal)
    
    def recuperar(self, ident):
        return self.dados.recuperar(ident)
    
    def listarTudo(self):
        return self.dados.listarTudo()