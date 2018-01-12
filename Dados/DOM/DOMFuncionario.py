from GerarId import *
from GerarArquivo import *
from Entidades.Funcionario import *
from Entidades.Gerente import *
from Negocio.Excecoes import *

class DOMFuncionario(object):
    def __init__(self, caminho="dados/banco/Funcionarios", nomeArq="Funcionarios"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ","
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
    def __criarObjeto(self, dados):
        saida = Funcionario(dados[1], dados[2], dados[3], dados[4], dados[0])
        
        if dados[5] == "True":
            saida = Gerente(saida)
        return saida
    
    def __criarLinha(self, funcionario):
        isGerente = False
        if isinstance(funcionario, Gerente):
            isGerente = True
        linha = str(funcionario.getIdent()) + self.separador
        linha += str(funcionario.getCpf()) + self.separador
        linha += str(funcionario.getNome()) + self.separador
        linha += str(funcionario.getSenha()) + self.separador
        linha += str(funcionario.getPis()) + self.separador
        linha += str(isGerente) + self.separador
        return linha
            
    def salvar(self, funcionario):
        
        if not isinstance(funcionario , Funcionario):
            raise TipoInvalidoException("Nao e um funcionario")
        
        
        ident = GerarId().proximo()
        funcionario.setIdent(ident)
        linha = self.__criarLinha(funcionario)
        linha +=  "\n"
        arquivo = open(self.caminho + self.nomeArq, 'a')
        
        arquivo.write(linha)
        arquivo.close()
        return funcionario
    
    def buscarPorCpf(self, cpf):
        cpf = str(cpf)
        funcionario = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        arquivo.close()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[1]) == cpf:
                funcionario = self.__criarObjeto(linha)
        return funcionario
    
    def buscarPorPis(self, pis):
        pis = str(pis)
        funcionario = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        arquivo.close()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[4]) == pis:
                funcionario = self.__criarObjeto(linha)
        return funcionario
    
    def recuperar(self, ident):
        ident = int(ident)
        funcionario = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        arquivo.close()
        for linha in linhas:
            linha = linha.split(self.separador)
            if int(linha[0]) == ident:
                funcionario = self.__criarObjeto(linha)
        return funcionario
    
    def alterar(self, funcionario):
        
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for i in range(len(linhas)):
            linha = linhas[i].split(self.separador)
            if int(linha[0]) == funcionario.getIdent():
                linhas[i] = self.__criarLinha(funcionario)
                break
        arquivo.close()
        arquivo = open(self.caminho + self.nomeArq,"w")
        arquivo.writelines(linhas)
        arquivo.close()
        return funcionario
    
    def listarTodosGerentes(self):
        listaGerentes = []
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        arquivo.close()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[5]) == "True":
                 listaGerentes.append(self.__criarObjeto(linha))
        return listaGerentes
