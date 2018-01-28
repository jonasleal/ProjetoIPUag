#Entidades

from Entidades.Tipo import *
from Entidades.Roupa import *
from Entidades.Estilo import *
from Entidades.Cliente import *
from Entidades.Gerente import *
from Entidades.Usuario import *
from Entidades.Funcionario import *
from Entidades.Compra import *
#DOMs
from Dados.DOM.DOMCliente import *
from Dados.DOM.DOMFuncionario import *
from Dados.DOM.DOMTipo import *
from Dados.DOM.DOMEstilo import *
from Dados.DOM.DOMPedido import *
from Dados.DOM.DOMCompra import *

from Dados.RepositorioCompra import *
#Negocio
from Negocio.GestaoCliente import *
from Negocio.GestaoEstoque import *
from Negocio.GestaoFuncionario import *
from Negocio.GestaoCompra import *
#Excecoes
from Negocio.Excecoes import *
#Fachada
from Fachada.Fachada import *

#Clientes
#cpf, nome, senha
cli1 = Cliente("106", "Jonas", "106")
cli2 = Cliente("549", "Ferreira", "549")

#Funcionarios
#cpf, nome, senha, pis,
fun1 = Funcionario("014", "Leal","014", "pis014")

#Tipos e estilo
tipo1 = Tipo("Blusa")
tipo2 = Tipo("Calca")

estilo1 = Estilo("Casual")
estilo2 = Estilo("Esportivo")
estilo3 = Estilo("Classico")

#Roupas
#nome, tamanho, estilo, tipo, genero, valor, quantidade = 0,desconto = 0
roupa1 = Roupa("roupa1", "G", Estilo("",4), Tipo("",3),"masculino", 50, 10)
roupa2 = Roupa("roupa2", "P", Estilo("",4), Tipo("",3),"masculino", 30, 20)

#Pedidos
#roupa, cliente, funcionario, quantidade = 1, ident




##Cadastros
#cli1 = Fachada().cadastrarCliente(cli1)
#fun1 = Fachada().cadastrarFuncionario(fun1)
#tipo1 = Fachada().cadastrarTipo(tipo1)
#estilo1 = Fachada().cadastrarEstilo(estilo1)
#roupa1 = Fachada().cadastrarRoupa(roupa1, 100)
#roupa2 = Fachada().cadastrarRoupa(roupa2, 100)
#roupa2 = Fachada().cadastrarRoupaOferta(roupa2, 50)
#fachada = Fachada()
#roupa1.setID(5)
#ped1 = Pedido(roupa1, Cliente("","","", 1), Funcionario("014", "Leal","014", "pis014", 2), 1)
#ped2 = Pedido(roupa1, Cliente("","","", 1), Funcionario("014", "Leal","014", "pis014", 2), 1)
#ped3 = Pedido(roupa1, Cliente("","","", 1), Funcionario("014", "Leal","014", "pis014", 2), 1)
#ped4 = Pedido(roupa1, Cliente("","","", 1), Funcionario("014", "Leal","014", "pis014", 2), 1)
#fachada.addCarrinho(ped1)
#fachada.addCarrinho(ped2)
#fachada.addCarrinho(ped3)
#fachada.addCarrinho(ped4)
#fachada.finalizarCompra()
#
#lista = fachada.listarTodasCompras()
#for i in lista:
#    print i
dataInicial = datetime.datetime.strptime("2016-01-01", '%Y-%m-%d')
dataFinal = datetime.datetime.strptime("2019-01-30", '%Y-%m-%d')
periodo = Fachada().relatorioLucroPorPeriodo(dataInicial, dataFinal)
lucroMes = periodo.lucroPorMes()
for i in lucroMes:
    print i 
