class RepositorioEstilo(object):
    def __init__(self, dados):
        self.dados = dados
    
    def salvar(self, tipo):
        return self.dados.salvar(tipo)
    
    def recuperar(self, ident):
        return self.dados.recuperar(ident)
    
    def buscarPorNome(self, nome):
        return self.dados.buscarPorNome(nome)
    
    def listarTodos(self):
        return self.dados.listarTodos()