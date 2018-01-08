from GerarId import *
from GerarArquivo import *
from Entidades.Cliente import *
from Negocio.Excecoes import *

class DOMCliente(object):
    def __init__(self, caminho="dados/banco/", nomeArq="Clientes"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        self.separador = ","
        GerarArquivo().criarPasta(self.caminho)
        GerarArquivo().criarArquivo(self.caminho,self.nomeArq)
            
    def salvar(self, cliente):
        
        if not isinstance(cliente , Cliente):
            raise TipoInvalidoException("Nao e um cliente")
        
        ident = GerarId().proximo()
        cliente.setIdent(ident)
        arquivo = open(self.caminho + self.nomeArq, 'a')
        linha = str(cliente.getIdent()) + self.separador
        linha += str(cliente.getCpf()) + self.separador
        linha += str(cliente.getNome()) + self.separador
        linha += str(cliente.getSenha()) + "\n"
        arquivo.write(linha)
        arquivo.close()
        return cliente
    
    def __criarCliente(self, dados):
        return Cliente(dados[1], dados[2], dados[3], dados[0])
    
    def buscarPorCpf(self, cpf):
        cpf = str(cpf)
        cliente = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if str(linha[1]) == cpf:
                cliente = self.__criarCliente(linha)
        return cliente
    
    def recuperar(self, ident):
        ident = int(ident)
        cliente = None
        arquivo = open(self.caminho + self.nomeArq,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.split(self.separador)
            if int(linha[0]) == ident:
                cliente = self.__criarCliente(linha)
        return cliente
        
#    def login(self, CpfCli, SenhaCli):
#        arq = open(self.caminho + self.nomeArq, 'r')
#        lista = arq.readlines()
#        usuario = None
#        for i in range(len(lista)):
#            iD = lista[i].split(self.separador)
#            if iD[1] == str(CpfCli) and iD[3] == SenhaCli:
#                usuario = self.__criarCliente(iD)
#        return usuario
        
