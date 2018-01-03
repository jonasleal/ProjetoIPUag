from Entidades.Roupa import *
from dados.RepositorioEstoque import *
from dados.DOM.DOMEstoque import *

class GestaoEstoque:

    def __init__:
        self.repEstoque = RepositorioEstoque(DOMEstoque())

    def CadastrarRoupaEstoque(self, roupa, quantidade):
        self.repEstoque.CadastrarRoupa(roupa, quantidade)
        
    def ListarRoupas(self):
        self.repEstoque.ListarRoupas()

    def ListarRoupasOferta(self):
        self.repEstoque.ListarRoupasOferta()

    def RecuperarRoupa(self, iD):
        self.repEstoque.RecuperarRoupa(iD)

    def RecuperarRoupa(self, iD):
        self.repEstoque.RecuperarRoupaOferta(iD)
    
    def CadastrarRoupasOferta(self, roupa, quantidade):
        self.repEstoque.CadastrarRoupaOferta(roupa, quantidade)

    def MaisVendidas(self):
