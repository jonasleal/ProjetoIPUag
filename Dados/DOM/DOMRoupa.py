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
        return Roupa(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6],dados[7], dados[8], dados[0])
        
    def __criarLinha(self, roupa):
        linha = str(roupa.getIdent()) +self.separador
        linha += str(roupa.getNome()) +self.separador
        linha += str(roupa.getTamanho()) +self.separador
        linha += str(roupa.getEstilo()) +self.separador
        linha += str(roupa.getTipo()) +self.separador
        linha += str(roupa.getGenero()) +self.separador
        linha += str(roupa.getValor()) +self.separador
        linha += str(roupa.getDesconto()) +self.separador
        linha += str(roupa.getQuantidade()) +self.separador
        return linha
    
    
    def listarTodos(self):
        listaRoupas = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            listaRoupas.append(self.__criarObjeto(linha))
        return listaRoupas
        
    def salvar(self, roupa, quantidade):
        
        quantidade = int(quantidade)
        
        if not isinstance(roupa , Roupa):
            raise RoupaInvalidoException("Nao e um roupa")
        
        ident = GerarId().proximo()
        roupa.setIdent(ident)
        linha = self.__criarLinha(roupa)
        linha = quantidade + self.separador
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
        
                
    def salvarOferta(self, roupa, desconto):
        if not isinstance(roupa , Roupa):
            raise RoupaInvalidoException("Nao e um roupa")
        roupa = self.recuperar(roupa.getID())
        roupa.setDesconto(desconto)
        return self.alterar(roupa)
        
        
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
        
    
