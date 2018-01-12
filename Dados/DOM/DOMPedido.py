from GerarId import *
from GerarArquivo import *
from Entidades.Pedido import *
from Entidades.PedidoPersonalizado import *
from Negocio.Excecoes import *

class DOMCliente(object):
    def __init__(self, caminho="dados/banco/Cliente", nomeArq="Clientes"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ";"
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
        
    def __criarLinha(self, pedido):
        
        linha = str(pedido.getIdent()) + self.separador
        linha += str(pedido.getRoupa()) + self.separador
        linha += str(pedido.getCliente()) + self.separador
        linha += str(pedido.getQuantidade()) + self.separador
        if isinstance(pedido, PedidoPersonalizado):
            linha += str(pedido.getMedidas()) + self.separador
            linha += str(pedido.getObservacoes()) + self.separador
        return linha
    
    def __criarObjeto(self, dados):
        saida = None
        if len(dados) < 6:
            saida = Peido(dados[1], dados[2], dados[3], dados[0])
        else:
            saida = PedidoPersonalizado(dados[1], dados[2], dados[3], dados[4], dados[5], dados[0])
        return saida 
            
    def salvar(self, pedido):
        
        if not isinstance(pedido , Cliente):
            raise TipoInvalidoException("Nao e um pedido")
        
        ident = GerarId().proximo()
        pedido.setIdent(ident)
        arquivo = open(self.caminho + self.nomeArq, 'a')
        linha = self.__criarLinha(pedido)
        linha +=  "\n"
        arquivo.write(linha)
        arquivo.close()
        return pedido
    
    
    
    def buscarPorCliente(self, cliente):
        if not isinstance(cliente , Cliente):
            raise TipoInvalidoException("Nao e um cliente")
        pedido = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[1]) == cliente.getIdent():
                pedido.appedn(self.__criarObjeto(linha))
        arquivo.close()
        return pedido
    
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
