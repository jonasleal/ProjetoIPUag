class RepositorioFuncionario(object):
    def __init__(self, dados):
        self.dados = dados
        
    def salvar(self, funcionario):
        return self.dados.salvar(funcionario)
    
    def buscarPorCpf(self, cpf):
        return self.dados.buscarPorCpf(cpf)
    
    def buscarPorPis(self, pis):
        return self.dados.buscarPorPis(pis)
    
    def recuperar(self, ident):
        return self.dados.recuperar( ident)

    def alterar(self,funcionario):
        return self.dados.alterar(funcionario)
    
    def listarTodosGerentes(self):
        return self.dados.listarTodosGerentes()