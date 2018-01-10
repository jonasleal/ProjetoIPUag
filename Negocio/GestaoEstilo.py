from Negocio.Excecoes import *
from Entidades.Estilo import *
from Dados.DOM.DOMEstilo import *
from Dados.RepositorioEstilo import *
class GestaoEstilo(object):
    def __init__(self):
        self.repEstilo = RepositorioEstilo(DOMEstilo())
    
    def cadastrar(self, estilo ):
        if not isinstance(estilo, Estilo):
            raise TipoInvalidoException("Nao e um estilo de roupa")
        
        tempEstilo = self.repEstilo.buscarPorNome(estilo.getNome())
        
        if tempEstilo != None:
            raise JaCadastradoException("Estilo %s ja cadastrado." % (estilo.getNome()))
        return self.repEstilo.salvar(estilo)
    
    def recuperar(self, ident):
        ident = int(ident)
        return self.repEstilo.recuperar(ident)
    
    def buscarPorNome(self, nome):
        nome = str(nome)
        return self.repEstilo.buscarPorNome(nome)
    
    def listarTodos(self):
        return self.repEstilo.listarTodos()