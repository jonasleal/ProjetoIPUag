class Oferta:

    def __init__(self, desconto = 0):
        self.__desconto = desconto

    def getDesconto(self):
        return self.__desconto

    def setDesconto(self, NovoDesconto):
        self.__desconto = NovoDesconto
    def __str__(self):
        return "%s%" % (self.__desconto)