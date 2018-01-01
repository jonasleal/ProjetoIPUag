from negocio.Excecoes import *
from entidades.Funcionario import *
from dados.DOM.DOMFuncionario import *
from dados.RepositorioFuncionario import *

class GestaoCliente(object):
    def __init__(self):
        self.repFuncionario = RepositorioFuncionario(DOMFuncionario())
    
    def cadastrar(self, funcionario):
        
        if not isinstance(funcionario, Cliente):
            raise TipoInvalidoException("Nao e um funcionario")
        
        tempFuncionario = self.repFuncionario.buscarPorCpf(funcionario.getCpf())
        
        if tempFuncionario != None:
            raise JaCadastradoException("CPF %s ja cadastrado." % (funcionario.getCpf()))
        
        return self.repFuncionario.salvar(funcionario)
    
    def recuperarPorCpf(self, cpf):
        
        cpf = str(cpf)
        return self.repFuncionario.buscarPorCpf(cpf)
    
    def recuperarPorPis(self, pis):
        
        pis = str(pis)
        return self.repFuncionario.buscarPorPis(pis)
    
    def login(self,cpf , senha):
        cpf = str(cpf)
        senha = str(senha)
        funcionario = self.repFuncionario.buscarPorCpf(cpf)
        
        if funcionario == None:
            raise CpfInvalidoException("CPF informado nao encontrado")
        elif funcionario.getSenha() != senha:
            raise SenhaInvalidoException("Senha informado nao corresponde")
        
        return funcionario