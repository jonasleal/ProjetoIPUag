class RepositorioEstoque(object):

    def __init__(self, dados):
        self.dados = dados
        
    def CadastrarRoupa(self, roupa):
        return self.dados.salvar(roupa)

    def alterar(self, roupa):
        return self.dados.alterar(roupa)
    
    def RecuperarRoupa(self, iD):
        return self.dados.recuperar(iD)

    def ListarRoupas(self):
        return self.dados.listarTodos()

    def ListarOfertas(self):
        return self.dados.listarOfertas()

    
