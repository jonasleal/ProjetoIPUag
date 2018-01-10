from Entidades.Tipo import *
from Entidades.Estilo import *
from Entidades.Usuario import *
from Entidades.Gerente import *
from Entidades.Funcionario import *
from Fachada.Fachada import *
from Negocio.Excecoes import *

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
    
    def __dadosTipo(self):
        nome = raw_input("Tipo: ")
        return Tipo(nome)
    
    def __dadosEstilo(self):
        nome = raw_input("Estilo: ")
        return Estilo(nome)
    
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
    
    def primeiroAcesso(self):
        try:
            return Fachada().primeiroAcesso()
        except(JaCadastradoException, TipoInvalidoException)as e:
            print e.getMessage()
            
    def tipo(self):
        try:
            tipo = self.__dadosTipo()
            return Fachada().cadastrarTipo(tipo)
        except(JaCadastradoException, TipoInvalidoException)as e:
            print e.getMessage()
            
    def estilo(self):
        try:
            estilo = self.__dadosEstilo()
            return Fachada().cadastrarEstilo(estilo)
        except(JaCadastradoException, TipoInvalidoException)as e:
            print e.getMessage()
            