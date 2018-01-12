from GerarId import *
from GerarArquivo import *
from Entidades.Roupa import *
from Negocio.Excecoes import *

class DOMRoupa(object):
    
    def __init__(self, caminho="dados/banco/Estoque", nomeArq="Roupas"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ";"
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
        
    def __criarObjeto(self, dados):
        return Roupa(dados[1], dados[0])
        
    def __criarLinha(self, roupa):
        linha = str(roupa.getIdent()) +self.separador
        linha += str(roupa.getNome()) +self.separador
        linha += str(roupa.getTamanho()) +self.separador
        linha += str(roupa.getGenero()) +self.separador
        linha += str(roupa.getValor()) +self.separador
        linha += str(roupa.getDesconto()) +self.separador
        return linha
        
    def salvar(self, roupa):
        
        if not isinstance(roupa , Roupa):
            raise RoupaInvalidoException("Nao e um roupa")
        
        ident = GerarId().proximo()
        roupa.setIdent(ident)
        linha = self.__criarLinha(roupa)
        linha +=  "\n"
        arquivo = open(self.caminho + self.nomeArq, 'a')
        
        arquivo.write(linha)
        arquivo.close()
        print roupa.getIdent()
        return roupa
    
    def recuperar(self, ident):
        ident = int(ident)
        roupa = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if int(linha[0]) == ident:
                roupa = self.__criarObjeto(linha)
        return roupa
    
    def buscarPorNome(self, nome):
        nome = str(nome)
        roupa = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[1]) == nome:
                roupa = self.__criarObjeto(linha)
        return roupa
        
    
    def listarTodos(self):
        listaRoupas = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            listaRoupas.append(self.__criarObjeto(linha))
        return listaRoupas
