from GerarId import *
from GerarArquivo import *
from Entidades.Pedido import *

from Dados.DOM.DOMCliente import *
from Dados.DOM.DOMRoupa import *
from Dados.DOM.DOMFuncionario import *
from Entidades.PedidoPersonalizado import *
from Negocio.Excecoes import *

class DOMPedido(object):
    def __init__(self, caminho="dados/banco/Vendas/", nomeArq="Pedidos"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ";"
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
        
    def __criarLinha(self, pedido):
        
        linha = str(pedido.getIdent()) + self.separador
        linha += str(pedido.getRoupa().getID()) + self.separador
        linha += str(pedido.getCliente().getIdent()) + self.separador
        linha += str(pedido.getFuncionario().getIdent()) + self.separador
        linha += str(pedido.getQuantidade()) + self.separador
        if isinstance(pedido, PedidoPersonalizado):
            linha += str(pedido.getMedidas()) + self.separador
            linha += str(pedido.getObservacoes()) + self.separador
        return linha
    
    def __criarObjeto(self, dados):
        saida = None
        cliente = DOMCliente().recuperar(dados[2])
        roupa = DOMRoupa().recuperar(dados[1])
        funcionario = DOMFuncionario().recuperar(dados[3])
        saida = Pedido(roupa, cliente, funcionario, dados[4], dados[0])
        if len(dados) > 6:
            saida = PedidoPersonalizado(saida, dados[5], dados[6])
        return saida 
            
    def salvar(self, pedido):
        
        ident = GerarId().proximo()
        pedido.setIdent(ident)
        arquivo = open(self.caminho + self.nomeArq, 'a')
        linha = self.__criarLinha(pedido)
        linha +=  "\n"
        arquivo.write(linha)
        arquivo.close()
        return pedido
    
    
    
    def buscarPorCliente(self, cliente):
        pedidos = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[2]) == cliente.getIdent():
                pedido.appedn(self.__criarObjeto(linha))
        arquivo.close()
        return pedidos
    
    def recuperar(self, ident):
        ident = int(ident)
        pedido = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if int(linha[0]) == ident:
                pedido = self.__criarObjeto(linha)
        arquivo.close()
        return pedido
