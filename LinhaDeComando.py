from UI.LoginUsuario import *
from UI.Cadastrar import *
from UI.Listar import *
from Entidades.Gerente import *
separador = "\n--------------------------------\n"
def mostrarMenu(msg):
    global separador
    print separador
    print msg
    try:
        opc = int(raw_input("Digite uma opcao: "))
        return opc    
    except(ValueError):
        print "Digite uma das opcoes listadas"
    
        
def menuGerente( gerente):
    msg = "1 - Cadastrar funcionario \n2 - Listar funcionarios \n3 - Promover funcionario \n4 - Cadastrar oferta\n0 - LogOut\n"
    global separador
    opc = -1
    print "Bem Vindo %s" %(gerente.getPrimeiroNome())
    
    while opc != 0:
        opc = mostrarMenu(msg)
        print separador
        if opc == 0:
            print "Logout"
        elif opc == 1:
            Cadastrar().funcionario()
        elif opc == 2:
            Listar().funcionarios()
        print separador
        
def menuFuncionario(funcionario):
    global separador
    print separador
    print "Bem Vindo %s" %(funcionario.getPrimeiroNome())
    msg = "1- Cadastrar cliente\n2- Cadastrar roupa\n3- Cadastrar estilo\n4- Cadastrar tipo\n0 - LogOut\n"
    opc = -1
    while opc != 0:
        opc = mostrarMenu(msg)
        print separador
        if opc == 0:
            print "Logout"
        elif opc == 1:
           Cadastrar().cliente()
        elif opc == 2:
            Cadastrar().roupa()
        elif opc == 3:
            Cadastrar().estilo()
        elif opc == 4:
            Cadastrar().tipo()
        elif opc == 4:
            print "nao implementado"
        
        

def menuPrincipal():
    global separador
    msg = "1 - Login como Funcionario\n2 - Login como Gerente\n4 - Listar Gerentes\n5 - Primeiro Acesso\n0 - Encerrar Sistema"
    opc = -1
    while opc !=0:
        opc = mostrarMenu(msg)
        print separador
        if opc == 0:
            print "FIM"
        elif opc == 1:
            funcionario = LoginUsuario().funcionario()
            if funcionario:
                    menuFuncionario(funcionario)
        elif opc == 2:
            gerente = LoginUsuario().gerente()
            if gerente:
                menuGerente(gerente)
#        elif opc == 3:
#            cliente = LoginUsuario().cliente()
#            if cliente:
#                menuCliente(cliente)
        elif opc == 4:
            Listar().gerentes()
        elif opc == 5:
           Cadastrar().primeiroAcesso()
        else:
            print "Digite uma opcao valida."
            print separador

menuPrincipal()