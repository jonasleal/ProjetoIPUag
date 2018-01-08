class RepositorioEstoque(object):

    def __init__(self, dados):
        self.dados = dados
        
    def CadastrarRoupa(self, roupa, quantidade):
        return self.dados.CadastrarRoupa(roupa, quantidade)

    def CadastrarRoupaOferta(self, roupa, quantidade):
        return self.dados.CadastrarRoupaOferta(roupa, quantidade)
    
    def RecuperarRoupa(self, iD):
        return self.dados.RecuperarRoupa(iD)

    def RecuperarRoupaOferta(self, iD):
        return self.dados.RecuperarRoupaOferta(iD)
    
    def ListarRoupas(self):
        return self.dados.ListarRoupas()

    def ListarRoupas(self):
        return self.dados.ListarRoupasOferta()

    
