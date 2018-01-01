from GerarId import *
from GerarArquivo import *
from Entidades.Funcionario import *
from negocio.Excecoes import *

class DOMFuncionario(object):
    def __init__(self, caminho="dados/banco/", nomeArq="Funcionarios"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ","
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
            
    def salvar(self, funcionario):
        
        if not isinstance(funcionario , Funcionario):
            raise TipoInvalidoException("Nao e um funcionario")
        
        ident = GerarId().proximo()
        funcionario.setIdent(ident)
        arquivo = open(self.caminho + self.nomeArq, 'a')
        linha = str(funcionario.getIdent()) + self.separador
        linha += str(funcionario.getCpf()) + self.separador
        linha += str(funcionario.getNome()) + self.separador
        linha += str(funcionario.getSenha()) + self.separador
        linha += str(funcionario.getPis()) + self.separador + "\n"
        arquivo.write(linha)
        arquivo.close()
        return funcionario
    
    def __criarFuncionario(self, dados):
        return Funcionario(dados[1], dados[2], dados[3], dados[4], dados[0])
    
    def buscarPorCpf(self, cpf):
        cpf = str(cpf)
        funcionario = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[1]) == cpf:
                funcionario = self.__criarFuncionario(linha)
        return funcionario
    
    def buscarPorPis(self, pis):
        pis = str(pis)
        funcionario = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[4]) == pis:
                funcionario = self.__criarFuncionario(linha)
        return funcionario
    
    def recuperar(self, ident):
        ident = int(ident)
        funcionario = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if int(linha[0]) == ident:
                funcionario = self.__criarFuncionario(linha)
        return funcionario
   