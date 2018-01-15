#Entidades
from Entidades.Cliente import *
from Entidades.Gerente import *
from Entidades.Usuario import *
from Entidades.Funcionario import *
#DOMs
from Dados.DOM.DOMCliente import *
from Dados.DOM.DOMFuncionario import *
from Dados.DOM.DOMTipo import *
from Dados.DOM.DOMEstilo import *
#Negocio
from Negocio.GestaoCliente import *
from Negocio.GestaoFuncionario import *
#Excecoes
from Negocio.Excecoes import *
#Fachada
from Fachada.Fachada import *




def testarCliente(fachada, cliente):
    try:
        fachada.cadastrarCliente(cliente)
    except(TipoInvalidoException, JaCadastradoException) as e:
        print e.getMessage()

    try:
        logado = fachada.loginCliente(cliente)
        print logado.getIdent()
    except (CpfInvalidoException, SenhaInvalidoException) as e:
        print e.getMessage()
        
def testarFuncionario(fachada, funcionario):
    try:
        fachada.cadastrarFuncionario(funcionario)
    except(TipoInvalidoException, JaCadastradoException) as e:
        print e.getMessage()

    try:
        logado = fachada.loginFuncionario(funcionario)
        print logado.getIdent()
        print isinstance(logado , Gerente)
        return logado
    except (CpfInvalidoException, SenhaInvalidoException) as e:
        print e.getMessage()

def testarPromover(fachada, funcionario):
    try:
        funcionario = fachada.promoverFuncionario(funcionario)
    except ( TipoInvalidoException) as e:
        print e.getMessage()
    return funcionario

def testarRevogarPromocao(fachada, funcionario):
    try:
        funcionario = fachada.revogarGerencia(funcionario)
    except ( TipoInvalidoException) as e:
        print e.getMessage()
    return funcionario
        
#f = Funcionario("123456", "Jonas","password", "654321")
#f2 = Funcionario("824", "Jonas", "654321", "password")
#c = Cliente("106", "Jonas Jr", "senha")
#fachada = Fachada()
#
#print "------ Cliente --------"
#testarCliente(fachada, c)
#print "------ Funcionario --------"
#testarFuncionario(fachada, f2)
#f = testarFuncionario(fachada, f)
#print "------ Promover --------"
#f = testarPromover(fachada, f)
#print type(f)
#print "------ Despromover --------"
#f = testarRevogarPromocao(fachada, f)
#print type(f)
#print "fim"

#Fachada().cadastrarTipo(Tipo("Calca"))
Fachada().cadastrarEstilo(Estilo("Casual"))

tipos = Fachada().listarTodosTipos()
for tipo in tipos:
    print tipo.getIdent()

estilos = Fachada().listarTodosEstilos()
for estilo in estilos:
     print estilo.getIdent()
