from negocio.Excecoes import *
from entidades.Cliente import *
from entidades.Gerente import *
from entidades.Usuario import *
from dados.DOM.DOMCliente import *
from entidades.Funcionario import *
from dados.RepositorioCliente import *
from negocio.GestaoCliente import *

f = Funcionario("123456", "Jonas","password", "654321")
g = Gerente("123456", "Jonas", "654321", "password")
c = Cliente("106", "Jonas Jr", "senha")

gCliente = GestaoCliente()

try:
    gCliente.cadastrar(c)
except(TipoInvalidoException, JaCadastradoException) as e:
    print e.getMessage()

try:
    logado = gCliente.login("106", "senha")
    print logado.getIdent()
except (CpfInvalidoException, SenhaInvalidoException) as e:
    print e.getMessage()
print "fim"