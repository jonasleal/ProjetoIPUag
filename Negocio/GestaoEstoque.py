from Entidades.Roupa import *
from Dados.RepositorioEstoque import *
from Dados.RepositorioEstilo import *
from Dados.RepositorioTipo import *
from Dados.DOM.DOMTipo import *
from Dados.DOM.DOMEstilo import *
from Dados.DOM.DOMRoupa import *
from Negocio.Excecoes import *

class GestaoEstoque:

    def __init__(self):
        self.repEstoque = RepositorioEstoque(DOMRoupa())
        self.repTipo = RepositorioTipo(DOMTipo())
        self.repEstilo = RepositorioEstilo(DOMEstilo())

    def CadastrarRoupaEstoque(self, roupa, quantidade):

        if not isinstance(roupa, Roupa):
            raise TipoInvalidoException("Nao eh uma roupa")
        estilo = self.repEstilo.recuperar(roupa.getEstilo().getIdent())
        tipo = self.repTipo.recuperar(roupa.getTipo().getIdent())
        if not isinstance(estilo, Estilo):
            raise NaoCadastradoException("Estilo nao cadastrado")
        if not isinstance(tipo, Tipo):
            raise NaoCadastradoException("Tipo nao cadastrado")
        
        
        roupa.setQuantidade(quantidade)
        return self.repEstoque.CadastrarRoupa(roupa)
    
    def RecuperarRoupa(self, iD):
        return self.repEstoque.RecuperarRoupa(iD)
    
    def saida(self, roupa, quantidade):
        if not isinstance(roupa, Roupa):
            raise TipoInvalidoException("Nao eh uma roupa")
        qAtual = self.RecuperarRoupa(roupa.getID()).getQuantidade()
        if qAtual < quantidade:
            raise QuantidadeIsuficienteException("Nao ha roupas suficiente para a venda no estoque.")
        roupa.setQuantidade((qAtual - quantidade))
        return self.repEstoque.alterar(roupa)
        
    def ListarRoupas(self):
        return self.repEstoque.ListarRoupas()

    def ListarRoupasOferta(self):
        return self.repEstoque.ListarOfertas()

    
    
    def CadastrarRoupasOferta(self, roupa, desconto):
        roupa.setDesconto(desconto)
        return self.repEstoque.alterar(roupa)
