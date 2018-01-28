import datetime
from Negocio.Excecoes import *
from Entidades.Periodo import *
from Dados.RepositorioCompra import *
from Dados.DOM.DOMCompra import *
class GestaoRelatorio(object):
    def __init__(self):
        self.repCompra = RepositorioCompra(DOMCompra())
    
    def lucroPorPeriodo(self, dataInicial, dataFinal):
        if not isinstance(dataInicial, date):
            TipoInvalidoException("Data inicial deve ser uma data")
        if not isinstance(dataFinal, date):
            TipoInvalidoException("Data final deve ser uma data")
            
        listaCompras = self.repCompra.recuperarPorPeriodo(dataInicial, dataFinal)
        
        return Periodo(listaCompras)
        