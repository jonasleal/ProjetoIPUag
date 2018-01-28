from GerarId import *
from GerarArquivo import *
from Dados.DOM.DOMPedido import *
from Entidades.Compra import *
from Negocio.Excecoes import *
import datetime

class DOMCompra(object):
    def __init__(self, caminho="dados/banco/Vendas/", nomeArq="Compras"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ";"
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
        
    def __criarLinha(self, objeto):
        
        linha = str(objeto.getIdent()) + self.separador
        pedidos = ""
        listaP = objeto.getPedidos()
        for i in range(len(listaP)):
            pedidos += str(listaP[i].getIdent())
            if i < (len(listaP) - 1):
                pedidos += ","
        linha += str(pedidos) + self.separador
        linha += str(objeto.getData()) + self.separador
        return linha
    
    def __criarObjeto(self, dados):
        domPedido = DOMPedido()
        saida = None
        idPedidos = dados[1].split(',')
        pedidos = []

        data = datetime.datetime.strptime(dados[2], '%Y-%m-%d %H:%M:%S.%f')
        for i in idPedidos:
            pedido = domPedido.recuperar(i)
            pedidos.append(pedido)
        saida = Compra(pedidos, data, dados[0])
        return saida 
            
    def salvar(self, compra):
        
        ident = GerarId().proximo()
        compra.setIdent(ident)
        arquivo = open(self.caminho + self.nomeArq, 'a')
        linha = self.__criarLinha(compra)
        linha +=  "\n"
        arquivo.write(linha)
        arquivo.close()
        return compra
    
    def recuperarPorPeriodo(self, dataInicial, dataFinal):
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        saida = []
        dataInicial = dataInicial.date()
        dataFinal = dataFinal.date()
        for linha in linhas:
            linha = linha.split(self.separador)
            data = datetime.datetime.strptime(linha[2], '%Y-%m-%d %H:%M:%S.%f')
            if dataInicial <= data.date()  <= dataFinal:
                compra = self.__criarObjeto(linha)
                saida.append(compra)
        return saida
            
            
        
            
            
    def buscarPorCliente(self, cliente):
        pedidos = DOMPedido().buscarPorCliente(cliente)
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        saida = []
        for linha in linhas:
            linha = linha.split(self.separador)
            linha[1] = linha[1].split(",")
            for i in linha[1]:
                for j in pedidos:
                    if int(i) == j.getIdent():
                        pedidos.remove(j)
                        saida.append(j)
        return saida
    
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
    
    def listarTudo(self):
        listaCompras = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            listaCompras.append(self.__criarObjeto(linha))
        return listaCompras
