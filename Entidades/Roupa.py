
class Roupa:

    def __init__(self, nome, tamanho, estilo, tipo, genero, valor, custo, quantidade = 0,desconto = 0, iD = 0):
        self.__nome = nome
        self.__tamanho = tamanho
        self.__estilo = estilo
        self.__tipo = tipo
        self.__valor = valor
        self.__iD = int(iD)
        self.__genero = genero
        self.__oferta = int(desconto)
        self.__quantidade = int(quantidade) 
        self.__custo = custo
    
    def getNome(self):
        return self.__nome

    def getTamanho(self):
        return self.__tamanho

    def getValor(self):
        return self.__valor
    
    def getCusto(self):
        return self.__custo

    def getID(self):
        return self.__iD

    def getGenero(self):
        return self.__genero
    
    def getEstilo(self):
        return self.__estilo

    def getTipo(self):
        return self.__tipo

    def getDesconto(self):
        return self.__oferta
    
    def getQuantidade(self):
        return self.__quantidade

    def setQuantidade(self, quantidade):
        self.__quantidade = quantidade
        
    def setDesconto(self, NovoDesconto):
        self.__oferta = int(NovoDesconto)

    def setID(self, iD):
        self.__iD = int(iD)
    
    def setValor(self, NovoValor):
        self.__valor = NovoValor
    
    def getPreco(self):
        saida = (self.__valor + (self.__valor * self.__oferta))
        return saida
