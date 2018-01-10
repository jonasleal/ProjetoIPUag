from GerarArquivo import GerarArquivo
import os

class __GeradorId(object):
    def __init__(self, caminho, nomeArq):
        self.caminho = caminho
        self.nomeArq = nomeArq
        GerarArquivo().criarPasta(self.caminho)
        
        try:
            os.stat(caminho + nomeArq)
        except:
            arquivo = open(caminho + nomeArq, 'w')
            arquivo.write("0")
            arquivo.close()
    def proximo(self):
        arquivo = open(self.caminho + self.nomeArq, 'r+')
        ident = int(arquivo.read())
        ident +=1
        arquivo.seek(0)
        arquivo.write(str(ident))
        arquivo.close()
        return ident
__instancia = None
def GerarId(caminho="dados/banco/Gerador", nomeArq="GeradorId.txt"):
    global __instancia
    if not __instancia:
        __instancia = __GeradorId(caminho, nomeArq)
    return __instancia
