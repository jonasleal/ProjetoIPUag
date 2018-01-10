from GerarId import *
from GerarArquivo import *
from Entidades.Roupa import *

class DOMEstoque(object):
    
    def __init__(self, caminho="dados/banco/Estoque", nomeArq="Roupas"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ";"
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
            
    def CadastrarRoupa(self, roupa, tipo, estilo, quantidade):

        ident = GerarId().proximo()
        roupa.setID(ident)
        arquivo = open(self.caminho + self.nomeArq, 'a')
        linha = str(roupa.getID()) + self.separador
        linha += str(roupa.getNome()) + self.separador
        linha += str(roupa.getTamanho()) + self.separador
        linha += str(roupa.getMedidas()) + self.separador
        linha += str(roupa.getGenero()) + self.separador
        linha += str(tipo.getNome()) + self.separador
        linha += str(estilo.getNome()) + self.separador
        linha += str(roupa.getValor()) + self.separador
        linha += str(roupa.getDesconto()) + self.separador
        linha += str(quantidade) + "\n"
        arquivo.write(linha)
        arquivo.close()

    def CadastrarRoupaOferta(self, roupa, tipo, estilo, quantidade):

        ident = GerarId().proximo()
        roupa.setID(ident)
        arquivo = open(self.caminho + 'RoupasOferta.txt', 'a')
        linha = str(roupa.getID()) + self.separador
        linha += str(roupa.getNome()) + self.separador
        linha += str(roupa.getTamanho()) + self.separador
        linha += str(roupa.getMedidas()) + self.separador
        linha += str(roupa.getGenero()) + self.separador
        linha += str(tipo.getNome()) + self.separador
        linha += str(estilo.getNome()) + self.separador
        linha += str(roupa.getValor()) + self.separador
        linha += str(roupa.getDesconto()) + self.separador
        linha += str(quantidade) + "\n"
        arquivo.write(linha)
        arquivo.close() 
    
    def RecuperarRoupa(self, iD):
        roupa = ''
        arquivo = open(self.caminho + self.nomeArq, 'r')
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if int(linha[0]) == iD:
                roupa = str(linha[0])+'-'+ str(linha[1])+'-'+ str(linha[2])+'-'+ str(linha[3])+'-'+ str(linha[4])
                roupa += '-'+ str(linha[5])+'-'+ str(linha[6])+'-'+ str(linha[7])+'-'+ str(linha[8])+'-'+ str(linha[9]).strip() 
        print roupa
        
    def RecuperarRoupaOferta(self, iD):
        roupa = ''
        arquivo = open(self.caminho + 'RoupasOferta.txt', 'r')
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if int(linha[0]) == iD:
                roupa = str(linha[0])+'-'+ str(linha[1])+'-'+ str(linha[2])+'-'+ str(linha[3])+'-'+ str(linha[4])
                roupa += '-'+ str(linha[5])+'-'+ str(linha[6])+'-'+ str(linha[7])+'-'+ str(linha[8])+'-'+ str(linha[9]).strip() 
        print roupa

    def ListarRoupas(self):
        arquivo = open(self.caminho + self.nomeArq, 'r')
        roupas = arquivo.readlines()
        for i in range(len(roupas)):
            print roupas[i].strip()
        arquivo.close()

    def ListarRoupasOferta(self):
        arquivo = open(self.caminho + 'RoupasOferta.txt', 'r')
        roupas = arquivo.readlines()
        for i in range(len(roupas)):
            print roupas[i].strip()
        arquivo.close()
