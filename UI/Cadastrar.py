from Entidades.Usuario import *
from Entidades.Gerente import *
from Entidades.Funcionario import *
from Fachada.Fachada import *
class Cadastrar(object):
    def __dadosUsuario(self):
        nome = raw_input("Nome completo: ")
        cpf = raw_input("CPF: ")
        senha = raw_input("Senha: ")
        return Usuario(cpf, senha, nome)
    
    def __dadosFuncionario(self):
        usuario = self.__dadosUsuario()
        pis = raw_input("PIS: ")
        return Funcionario(usuario.getCpf(), usuario.getNome(), usuario.getSenha(), pis)
    
    
    def cliente(self):
        try:
            usuario = self.__dadosUsuario()
            cliente = Cliente(usuario.getCpf(), usuario.getNome(), usuario.getSenha())
            return Fachada().cadastrarCliente( cliente)
        except(JaCadastradoException, TipoInvalidoException)as e:
            print e.getMessage()
    
    def funcionario(self):
        try:
            funcionario = self.__dadosFuncionario()
            return Fachada().cadastrarFuncionario( funcionario)
        except(JaCadastradoException, TipoInvalidoException)as e:
            print e.getMessage()
    
    def gerente(self):
        try:
            gerente = Gerente(self.__dadosFuncionario())
            return Fachada().cadastrarGerente( gerente)
        except(JaCadastradoException, TipoInvalidoException)as e:
            print e.getMessage()