class Carrinho(object):
    def __init__(self):
        self.lista = []
    def adicionar(self, pedido):
        self.lista.append(pedido)
    def remover(self, pedido):
        try:
            self.lista.remove(pedido)
            saida = True
        except(ValueError):
            saida = False
        return saida
    def listarTudo(self):
        return self.lista
    
    def __str__(self):
        return self.lista