from GerarId import *
from DOMTipo import *
from DOMEstilo import *
from GerarArquivo import *
from Entidades.Roupa import *
from Negocio.Excecoes import *

class DOMRoupa(object):
    
    def __init__(self, caminho="dados/banco/Estoque/", nomeArq="Roupas"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ";"
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
        
    def __criarObjeto(self, dados):
        estilo = DOMEstilo().recuperar(dados[3])
        tipo = DOMTipo().recuperar(dados[4])
        return Roupa(dados[1],dados[2],estilo,tipo,dados[5],dados[6],dados[7], dados[8], dados[9], dados[0])
        
    def __criarLinha(self, roupa):
        linha = str(roupa.getID()) +self.separador
        linha += str(roupa.getNome()) +self.separador
        linha += str(roupa.getTamanho()) +self.separador
        linha += str(roupa.getEstilo().getIdent()) +self.separador
        linha += str(roupa.getTipo().getIdent()) +self.separador
        linha += str(roupa.getGenero()) +self.separador
        linha += str(roupa.getValor()) +self.separador
        linha += str(roupa.getCusto()) +self.separador
        linha += str(roupa.getQuantidade()) +self.separador
        linha += str(roupa.getDesconto()) +self.separador 
        linha += "\n"
        
        return linha
    
    
    def listarTodos(self):
        listaRoupas = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            listaRoupas.append(self.__criarObjeto(linha))
        return listaRoupas
        
    def salvar(self, roupa):
        
        
        if not isinstance(roupa , Roupa):
            raise RoupaInvalidoException("Nao e um roupa")
        
        ident = GerarId().proximo()
        roupa.setID(ident)
        linha = self.__criarLinha(roupa)
        arquivo = open(self.caminho + self.nomeArq, 'a')
        
        arquivo.write(linha)
        arquivo.close()
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
    
    def alterar(self, roupa):
        
        if not isinstance(roupa , Roupa):
            raise RoupaInvalidoException("Nao e um roupa")
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for i in range(len(linhas)):
            linha = linhas[i].split(self.separador)
            if int(linha[0]) == roupa.getID():
                linhas[i] = self.__criarLinha(roupa)
                break
        arquivo.close()
        arquivo = open(self.caminho + self.nomeArq,"w")
        arquivo.writelines(linhas)
        arquivo.close()
        return roupa
     
        
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
        lista = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        arquivo.close()
        for linha in linhas:
            linha = linha.split(self.separador)
            lista.append(self.__criarObjeto(linha))
        return lista
          
    def listarOfertas(self):
        lista = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        arquivo.close()
        for linha in linhas:
            linha = linha.split(self.separador)
            roupa = self.__criarObjeto(linha)
            if roupa.getDesconto() > 0:
                    lista.append(roupa)
        return lista
