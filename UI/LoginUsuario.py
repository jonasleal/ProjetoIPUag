from Fachada.Fachada import *
from Entidades.Usuario import *
from Negocio.Excecoes import *

class LoginUsuario(object):
    def __logar(self):
        cpf = raw_input("Digite o CPF: ")
        senha = raw_input("Digite a senha: ")
        return Usuario(cpf, senha)
    
    def cliente(self):
        usuario = self.__logar()
        cliente = False
        try:
            cliente = Fachada().loginCliente(usuario)
        except (CpfInvalidoException, SenhaInvalidoException, TipoInvalidoException) as e:
            print e.getMessage()
        return cliente

    def funcionario(self):
        usuario = self.__logar()
        funcionario = False
        try:
            funcionario = Fachada().loginFuncionario(usuario)
        except (CpfInvalidoException, SenhaInvalidoException, TipoInvalidoException) as e:
            print e.getMessage()
        return funcionario

    def gerente(self):
        usuario = self.__logar()
        gerente = False
        try:
            gerente = Fachada().loginGerente(usuario)
        except (CpfInvalidoException, SenhaInvalidoException, TipoInvalidoException) as e:
            print e.getMessage()
        return gerente