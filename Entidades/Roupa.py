from Oferta import *

class Roupa:

    def __init__(self, nome, tamanho, genero, valor, desconto = 0, iD = 0):
        self.__nome = nome
        self.__tamanho = tamanho
        self.__valor = valor
        self.__iD = iD
        self.__genero = genero
        self.__oferta = Oferta(desconto) 
    
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

    def getDesconto(self):
        return self.__oferta.getDesconto()

    def setDesconto(self, NovoDesconto):
        self.__oferta.setDesconto(NovoDesconto)

    def setID(self, NovoID):
        self.__iD = NovoID
    
    def setValor(self, NovoValor):
        self.__valor = NovoValor
