import os

class GerarArquivo(object):

    def __init__(self):
        pass
     
    def criarPasta(self,nome):

        try:
            os.stat(nome)
        except:
            os.makedirs(nome)
 
     
    def criarArquivo(self, caminho, nomeArq):
        try:
            os.stat(caminho + nomeArq)
        except:
            arquivo = open(caminho + nomeArq, 'w')
            arquivo.close()
    
