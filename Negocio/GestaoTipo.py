from Negocio.Excecoes import *
from Entidades.Tipo import *
from Dados.DOM.DOMTipo import *
from Dados.RepositorioTipo import *
class GestaoTipo(object):
    def __init__(self):
        self.repTipo = RepositorioTipo(DOMTipo())
    
    def cadastrar(self, tipo ):
        if not isinstance(tipo, Tipo):
            raise TipoInvalidoException("Nao e um tipo de roupa")
        
        tempTipo = self.repTipo.buscarPorNome(tipo.getNome())
        
        if tempTipo != None:
            raise JaCadastradoException("Tipo %s ja cadastrado." % (tipo.getNome()))
        return self.repTipo.salvar(tipo)
    
    def recuperar(self, ident):
        ident = int(ident)
        return self.repTipo.recuperar(ident)
    
    def buscarPorNome(self, nome):
        nome = str(nome)
        return self.repTipo.buscarPorNome(nome)
    
    def listarTodos(self):
        return self.repTipo.listarTodos()