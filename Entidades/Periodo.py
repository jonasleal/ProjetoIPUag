
from Entidades.LucroMes import *

class Periodo(object):
    def __init__(self, dados = []):
        self.dados = dados
    
    def adicionarDados(self, dado):
        self.dados.append(dado)
    
    def lucroPorMes(self):
        lucroMes = []
         
       
       
        for dado in self.dados:
            data = dado.getData()
            adicionou = False
            for i in range(len(lucroMes)):
                
                if lucroMes[i].getMes() == data.date().strftime("%m-%Y"):
                    lucroMes[i].addLucro(dado.getValor())
                    adicionou = True
            if not adicionou:
                lucroMes.append(LucroMes(dado.getData(), dado.getValor()) )
                
#            
#            try:
#                meses[i.getData().strftime("%m-%Y")] += i.detValor()
#                print somou
#            except:
#                meses.update({i.getData().strftime("%m-%Y") : i.getValor()})
        return lucroMes
    
    def __str__(self):
        saida = "Periodo: "
        for i in self.dados:
            saida += i
            saida += ","
        return saida