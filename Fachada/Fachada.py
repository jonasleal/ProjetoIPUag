from Negocio.GestaoCliente import *
from Negocio.GestaoFuncionario import *

class Fachada(object):
    def __init__(self):
        self.gCliente = GestaoCliente()
        self.gFuncionario = GestaoFuncionario()
        
    def cadastrarCliente(self, cliente):
        return self.gCliente.cadastrar(cliente)
        
    def loginCliente(self, usuario):
        return self.gCliente.login(usuario)
        
    def cadastrarFuncionario(self, funcionario):
        return self.gFuncionario.cadastrar(funcionario)
    
    def promoverFuncionario(self, funcionario):
        return self.gFuncionario.tornarGerente(funcionario)
    
    def revogarGerencia(self, funcionario):
        return self.gFuncionario.revogarGerente(funcionario)
    
    def loginFuncionario(self, usuario):
        return self.gFuncionario.login(usuario)
    