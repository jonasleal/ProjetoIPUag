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
    
    #Cliente
    def cadastrarCliente(self, cliente):
        return self.gCliente.cadastrar(cliente)
        
    def loginCliente(self, usuario):
        return self.gCliente.login(usuario)
    
    #Funcionario
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
    
    #Roupa
    def cadastrarTipo(self, tipo):
        return self.gTipo.cadastrar(tipo)
    
    def listarTodosTipos(self):
        return self.gTipo.listarTodos()
    
    def cadastrarEstilo(self, estilo):
        return self.gEstilo.cadastrar(estilo)
    
    def listarTodosEstilos(self):
        return self.gEstilo.listarTodos()
    
    def cadastrarRoupa(self, roupa, quantidade):
        return self.gEstoque.CadastrarRoupaEstoque(roupa, quantidade)
    
    def cadastrarRoupaOferta(self, roupa, desconto):
        return self.gEstoque.CadastrarRoupaEstoque(roupa, desconto)
    
    def listarRoupas(self):
        return self.gEstoque.ListarRoupas()
    
    def listarRoupasOferta(self):
        return self.gEstoque.ListarRoupasOferta()
    