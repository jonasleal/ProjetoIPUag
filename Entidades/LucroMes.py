class LucroMes(object):
    def __init__(self, data, lucro):
        self.mes = data.strftime("%m-%Y")
        self.lucro = lucro
    def getMes(self):
        return self.mes
    def getLucro(self):
        return self.lucro
    def addLucro(self, lucro):
        self.lucro += lucro
    def __cmp__(self, outro):
        saida = 0
        if self.mes > outro.getMes():
            saida = 1
        elif self.mes < outro.getMes():
            saida = -1
        return saida 
    def __str__(self):
        saida =  "Mes: %s" % ( self.mes)
        saida += "\n"
        saida +=  "Lucro: R$ %0.02f" % (self.lucro)
        return saida