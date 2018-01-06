class RepositorioCliente(object):
    def __init__(self, dados):
        self.dados = dados
        
    def salvar(self, cliente):
        return self.dados.salvar(cliente)
    
    def buscarPorCpf(self, cpf):
        return self.dados.buscarPorCpf(cpf)
    
    def recuperar(self, ident):
        return self.dados.recuperar( ident)
#    
#    def login(self, CpfCli, SenhaCli):

#        return self.dados.login( CpfCli, SenhaCli)