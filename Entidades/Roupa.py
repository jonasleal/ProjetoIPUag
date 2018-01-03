from Oferta import *
from Tipo import *

class Roupa(Oferta, Tipo):

    def __init__(self, nome, tamanho, tipo, genero, valor, desconto = 0, iD = 0):
        self.__nome = nome
        self.__tamanho = tamanho
        self.__valor = valor
        self.__iD = iD
        self.__genero = genero
        Tipo.__init__(self, tipo)
        Oferta.__init__(self, desconto)
    
    def getNome(self):
        return self.__nome

    def getTamanho(self):
        return self.__tamanho

    def getValor(self):
        return self.__valor

    def getID(self):
        return self.__iD

    def getGenero(self):
        return self.__genero
    
    def setGenero(self, NovoGenero):
        self.__genero = NovoGenero

    def setID(self, NovoID):
        self.__iD = NovoID
    
    def setValor(self, NovoValor):
        self.__valor = NovoValor
