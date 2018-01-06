from UI.LoginUsuario import *
from UI.Cadastrar import *

def mostrarMenu(msg):
    print msg
    try:
        opc = int(raw_input("Digite uma opcao: "))
        return opc    
    except(ValueError):
        print "Digite uma das opcoes listadas"
        
def menuGerente():
    msg = "1 - Cadastrar funcionario \n2 - Listar funcionarios \n3 - Promover funcionario \n4 - Cadastrar oferta\n0 - LogOut\n"
    opc = -1
    while opc != 0:
        opc = mostrarMenu(msg)
        
def menuFuncionario(funcionario):
    msg = "1- Cadastrar cliente\n2- Cadastrar roupa\n3- Cadastrar estilo\n4- \n0 - LogOut\n"
    opc = -1
    while opc != 0:
        opc = mostrarMenu(msg)
        if opc == 1:
           Cadastrar().cliente()
        elif opc == 2:
            Cadastrar().roupa()
        elif opc == 3:
            pass
        elif opc == 4:
            print "nao implementado"
        

def menuPrincipal():
    msg = "1 - Login como Funcionario\n2 - Login como Gerente\n3 - Login como Cliente\n4 - Listar Gerentes\n5 - Primeiro Acesso\n0 - Encerrar Sistema"
    opc = -1
    while opc !=0:
        opc = mostrarMenu(msg)
        if opc == 1:
            funcionario = LoginUsuario().funcionario()
            if funcionario:
                    menuFuncionario(funcionario)
        elif opc == 2:
            gerente = LoginUsuario().gerente()
            if gerente:
                menuGerente(gerente)
        elif opc == 3:
            cliente = LoginUsuario().cliente()
            if cliente:
                menuCliente(cliente)
        elif opc == 4:
            print "nao implementado"
        

menuPrincipal()