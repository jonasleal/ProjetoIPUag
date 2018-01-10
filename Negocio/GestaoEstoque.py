from Entidades.Roupa import *
from dados.RepositorioEstoque import *
from dados.DOM.DOMEstoque import *
from Negocio.Excecoes import *

class GestaoEstoque:

    def __init__:
        self.repEstoque = RepositorioEstoque(DOMEstoque())

    def CadastrarRoupaEstoque(self, roupa, tipo, estilo, quantidade):

        if not isinstance(roupa, Roupa):
            raise TipoInvalidoException("Nao eh uma roupa")
        
        return self.repEstoque.CadastrarRoupa(roupa, tipo, estilo, quantidade)
        
    def ListarRoupas(self):
        return self.repEstoque.ListarRoupas()

    def ListarRoupasOferta(self):
        return self.repEstoque.ListarRoupasOferta()

    def RecuperarRoupa(self, iD):
        return self.repEstoque.RecuperarRoupa(iD)

    def RecuperarRoupa(self, iD):
        return self.repEstoque.RecuperarRoupaOferta(iD)
    
    def CadastrarRoupasOferta(self, roupa, tipo, estilo, quantidade):
        return self.repEstoque.CadastrarRoupaOferta(roupa, tipo, estilo, quantidade)
