class RepositorioEstoque(object):

    def __init__(self, dados):
        self.dados = dados
        
    def cadastrar(self, roupa, quantidade):
        return self.dados.CadastrarRoupa(roupa, quantidade)

    def cadastrarRoupaOferta(self, roupa):
        return self.dados.CadastrarRoupaOferta(roupa, tipo, estilo, quantidade)
    
    def recuperarRoupa(self, iD):
        return self.dados.RecuperarRoupa(iD)

    def recuperarRoupaOferta(self, iD):
        return self.dados.RecuperarRoupaOferta(iD)
    
    def listarRoupas(self):
        return self.dados.ListarRoupas()

    def listarRoupas(self):
        return self.dados.ListarRoupasOferta()

    
