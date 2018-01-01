#Entidades
from entidades.Cliente import *
from entidades.Gerente import *
from entidades.Usuario import *
from entidades.Funcionario import *
#DOMs
from dados.DOM.DOMCliente import *
from dados.DOM.DOMFuncionario import *
#Negocio
from negocio.GestaoCliente import *
from negocio.GestaoFuncionario import *
#Excecoes
from negocio.Excecoes import *




def testarCliente(gCliente, cliente):
    try:
        gCliente.cadastrar(cliente)
    except(TipoInvalidoException, JaCadastradoException) as e:
        print e.getMessage()

    try:
        logado = gCliente.login(cliente.getCpf(), cliente.getSenha())
        print logado.getIdent()
    except (CpfInvalidoException, SenhaInvalidoException) as e:
        print e.getMessage()
        
def testarFuncionario(gFuncionario, funcionario):
    try:
        gFuncionario.cadastrar(funcionario)
    except(TipoInvalidoException, JaCadastradoException) as e:
        print e.getMessage()

    try:
        logado = gFuncionario.login(funcionario.getCpf(), funcionario.getSenha())
        print logado.getIdent()
    except (CpfInvalidoException, SenhaInvalidoException) as e:
        print e.getMessage()


f = Funcionario("123456", "Jonas","password", "654321")
g = Gerente("123456", "Jonas", "654321", "password")
c = Cliente("106", "Jonas Jr", "senha")

print "------ Cliente --------"
testarCliente(GestaoCliente(), c)
print "------ Funcionario --------"
testarFuncionario(GestaoFuncionario(), f)
print "fim"