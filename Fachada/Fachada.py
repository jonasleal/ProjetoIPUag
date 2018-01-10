from Negocio.GestaoTipo import *
from Negocio.GestaoEstilo import *
from Negocio.GestaoCliente import *
from Negocio.GestaoFuncionario import *

class Fachada(object):
    def __init__(self):
        self.gCliente = GestaoCliente()
        self.gTipo = GestaoTipo()
        self.gEstilo = GestaoEstilo()
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
    
    def primeiroAcesso(self):
        return self.gFuncionario.primeiroAcesso()
    
    def listarTodosGerentes(self):
        return self.gFuncionario.listarTodosGerentes()
    
    def listarTodosFuncionarios(self):
        return self.gFuncionario.listarTodosFuncionarios()
    
    def cadastrarTipo(self, tipo):
        return self.gTipo.cadastrar(tipo)
    
    def listarTodosTipos(self):
        return self.gTipo.listarTodos()
    
    def cadastrarEstilo(self, estilo):
        return self.gEstilo.cadastrar(estilo)
    
    def listarTodosEstilos(self):
        return self.gEstilo.listarTodos()