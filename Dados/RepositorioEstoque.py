class RepositorioEstoque(object):

    def __init__(self, dados):
        self.dados = dados
        
    def CadastrarRoupa(self, roupa, quantidade):
        return self.dados.salvar(roupa,  quantidade)

    def CadastrarRoupaOferta(self, roupa, quantidade):
        return self.dados.salvarOferta(roupa, quantidade)
    
    def RecuperarRoupa(self, iD):
        return self.dados.recuperar(iD)

    def ListarRoupas(self):
        return self.dados.ListarRoupas()

    def ListarOfertas(self):
        return self.dados.ListarRoupasOferta()

    
