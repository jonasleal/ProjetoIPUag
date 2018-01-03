from Funcionario import *
class Gerente(Funcionario):
    def __init__(self, funcionario):
        super(Gerente, self).__init__(funcionario.getCpf(), funcionario.getNome(), funcionario.getSenha(), funcionario.getPis(), funcionario.getIdent())
    