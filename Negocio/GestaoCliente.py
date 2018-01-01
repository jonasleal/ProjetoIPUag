from negocio.Excecoes import *
from entidades.Cliente import *
from dados.DOM.DOMCliente import *
from dados.RepositorioCliente import *

class GestaoCliente(object):
    def __init__(self):
        self.repCliente = RepositorioCliente(DOMCliente())
    
    def cadastrar(self, cliente):
        
        if not isinstance(cliente, Cliente):
            raise TipoInvalidoException("Nao e um cliente")
        
        tempCliente = self.repCliente.buscarPorCpf(cliente.getCpf())
        
        if tempCliente != None:
            raise JaCadastradoException("CPF %s ja cadastrado." % (cliente.getCpf()))
        
        return self.repCliente.salvar(cliente)
    
    def recuperar(self, cpf):
        
        cpf = str(cpf)
        return self.repCliente.buscarPorCpf(cpf)
    
    def login(self,cpf , senha):
        cpf = str(cpf)
        senha = str(senha)
        cliente = self.repCliente.buscarPorCpf(cpf)
        
        if cliente == None:
            raise CpfInvalidoException("CPF informado nao encontrado")
        elif cliente.getSenha() != senha:
            raise SenhaInvalidoException("Senha informado nao corresponde")
        
        return cliente