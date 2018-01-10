from Negocio.Excecoes import *
from Entidades.Funcionario import *
from Entidades.Usuario import *
from Dados.DOM.DOMFuncionario import *
from Dados.RepositorioFuncionario import *

class GestaoFuncionario(object):
    def __init__(self):
        self.repFuncionario = RepositorioFuncionario(DOMFuncionario())
    
    def cadastrar(self, funcionario):
        if not isinstance(funcionario, Funcionario):
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
    
    def login(self,usuario):
        if not isinstance(usuario, Usuario):
            raise TipoInvalidoException("Nao e um usuario")
        cpf = str(usuario.getCpf())
        senha = str(usuario.getSenha())
        
        funcionario = self.repFuncionario.buscarPorCpf(cpf)
        if funcionario == None:
            raise CpfInvalidoException("CPF informado nao encontrado")
        elif funcionario.getSenha() != senha:
            raise SenhaInvalidoException("Senha informado nao corresponde")
        
        return funcionario
    
    def tornarGerente(self, funcionario):
        if not isinstance(funcionario, Funcionario):
            raise TipoInvalidoException("Nao e um funcionario.")
        if isinstance(funcionario, Gerente):
            raise TipoInvalidoException("Ja e gerente.")
        gerente = Gerente(funcionario)
        return self.repFuncionario.alterar(gerente)
    
    def primeiroAcesso(self):
        listaGerentes = self.repFuncionario.listarTodosGerentes()
        if len(listaGerentes) == 0:
            funcionario = self.cadastrar(Funcionario("123", "Administrador", "123", "000"))
            return self.tornarGerente(funcionario)
        raise JaCadastradoException("Ja existe gerente cadastrado.")
        
    def revogarGerente(self, gerente):
        if not isinstance(gerente, Funcionario):
            raise TipoInvalidoException("Nao e um funcionario.")
        if not isinstance(gerente, Gerente):
            raise TipoInvalidoException("Nao e um gerente.")
        funcionario = Funcionario(gerente.getCpf(), gerente.getNome(),gerente.getSenha(), gerente.getPis(),  gerente.getIdent())
        return self.repFuncionario.alterar(funcionario)
    
    def listarTodosGerentes(self):
        return self.repFuncionario.listarTodosGerentes()
    
    def listarTodosFuncionarios(self):
        return self.repFuncionario.listarTodosFuncionarios()
        