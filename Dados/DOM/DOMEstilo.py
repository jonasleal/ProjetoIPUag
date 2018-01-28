from GerarId import *
from GerarArquivo import *
from Entidades.Estilo import *
from Negocio.Excecoes import *

class DOMEstilo(object):
    
    def __init__(self, caminho="dados/banco/Estoque/", nomeArq="Estilos"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ";"
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
        
    def __criarObjeto(self, dados):
        return Estilo(dados[1], dados[0])
        
    def __criarLinha(self, objeto):
        linha = str(objeto.getIdent()) +self.separador
        linha += str(objeto.getNome()) +self.separador
        return linha
        
    def salvar(self, estilo):
        if not isinstance(estilo , Estilo):
            raise TipoInvalidoException("Nao e um estilo de roupa")
        
        ident = GerarId().proximo()
        estilo.setIdent(ident)
        linha = self.__criarLinha(estilo)
        linha +=  "\n"
        arquivo = open(self.caminho + self.nomeArq, 'a')
        
        arquivo.write(linha)
        arquivo.close()
        return estilo
    
    def recuperar(self, ident):
        ident = int(ident)
        estilo = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if int(linha[0]) == ident:
                estilo = self.__criarObjeto(linha)
        return estilo
    
    def buscarPorNome(self, nome):
        nome = str(nome)
        estilo = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[1]) == nome:
                estilo = self.__criarObjeto(linha)
        return estilo
    
    def listarTodos(self):
        listaEstilos = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            listaEstilos.append(self.__criarObjeto(linha))
        return listaEstilos
