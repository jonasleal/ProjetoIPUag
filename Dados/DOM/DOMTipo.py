from GerarId import *
from GerarArquivo import *
from Entidades.Tipo import *
from Negocio.Excecoes import *
class DOMTipo(object):
    def __init__(self, caminho="dados/banco/", nomeArq="Tipos"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ","
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
        
    def __criarTipo(self, dados):
        return Tipo(dados[1], dados[0])
        
    def __criarLinha(self, tipo):
        linha = str(tipo.getIdent()) +self.separador
        linha += str(tipo.getNome()) +self.separador
        return linha
        
    def salvar(self, tipo):
        
        if not isinstance(tipo , Tipo):
            raise TipoInvalidoException("Nao e um tipo de roupa")
        
        ident = GerarId().proximo()
        tipo.setIdent(ident)
        linha = self.__criarLinha(tipo)
        linha +=  "\n"
        arquivo = open(self.caminho + self.nomeArq, 'a')
        
        arquivo.write(linha)
        arquivo.close()
        print tipo.getIdent()
        return tipo
    
    def recuperar(self, ident):
        ident = int(ident)
        tipo = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if int(linha[0]) == ident:
                tipo = self.__criarTipo(linha)
        return tipo
    
    def buscarPorNome(self, nome):
        nome = str(nome)
        tipo = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[1]) == nome:
                tipo = self.__criarTipo(linha)
        return tipo
        
    
    def listarTodos(self):
        listaTipos = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            listaTipos.append(self.__criarTipo(linha))
        return listaTipos