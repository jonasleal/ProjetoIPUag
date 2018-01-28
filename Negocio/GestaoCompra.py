from Dados.RepositorioPedido import *
from Dados.RepositorioCliente import *
from Dados.RepositorioFuncionario import *
from Dados.RepositorioCompra import *
from Entidades.Pedido import *
from Entidades.Cliente import *
from Entidades.Funcionario import *
from Entidades.Roupa import *
from Dados.DOM.DOMPedido import *
from Dados.DOM.DOMRoupa import *
from Dados.DOM.DOMCliente import *
from Dados.DOM.DOMCompra import *
from Dados.DOM.DOMFuncionario import *
from Entidades.Carrinho import *
from Negocio.Excecoes import *
from Negocio.GestaoEstoque import *

class GestaoCompra(object):
    def __init__(self):
        self.repPedido = RepositorioPedido(DOMPedido())
        self.repCliente = RepositorioCliente(DOMCliente())
        self.repCompra = RepositorioCompra(DOMCompra())
        self.repFuncionario = RepositorioFuncionario(DOMFuncionario())
        self.gEstoque = GestaoEstoque()
        self.carrinho = Carrinho()
        
    def adicionarCarrinho(self, pedido):
        if not isinstance(pedido , Pedido):
            raise TipoInvalidoException("Nao e um pedido")
        roupa = self.gEstoque.RecuperarRoupa(pedido.getRoupa().getID())
        cliente = self.repCliente.recuperar(pedido.getCliente().getIdent())
        funcionario = self.repFuncionario.recuperar(pedido.getFuncionario().getIdent())
        
        if not isinstance(roupa , Roupa):
            raise NaoCadastradoException("Roupa nao cadastrada")
        if not isinstance(cliente , Cliente):
            raise NaoCadastradoException("Cliente nao cadastrada")
        if not isinstance(funcionario , Funcionario):
            raise NaoCadastradoException("Funcionario nao cadastrada")
        
        return self.carrinho.adicionar(pedido)
    
    def finalizarCompra(self):
        compra = Compra()
        for pedido in self.carrinho.listarTudo():
            roupa = pedido.getRoupa()
            try:
                self.gEstoque.saida(roupa, pedido.getQuantidade())
                pedido = self.repPedido.salvar(pedido)
            
                compra.addPedido(pedido)
            except(QuantidadeIsuficienteException):
                pass
            
        if len(compra.getPedidos())< 1:
            raise CompraNaoRealizadaException("Compra nao realizada, nenhum pedido valido processado.")
        self.repCompra.salvar(compra)
        return compra
            
        
    def recuperar(self, ident):
        ident = int(ident)
        return self.repPedido.recuperar(ident)
    
    def recuperarPorCliente(self, cliente):
        if not isinstance(cliente , Cliente):
            raise TipoInvalidoException("Nao e um cliente")
        return self.repPedido.buscarPorCliente(cliente)
    
    def listarTodos(self):
        return self.repCompra.listarTudo()
        