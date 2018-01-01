
from GerarArquivo import GerarArquivo
class GeradorId(object):
    def __init__(self, caminho="banco/", nomeArq="GeradorId"):
        self.caminho = caminho
        self.nomeArq = nomeArq + ".txt"
        GerarArquivo().criarPasta(self.caminho)
        try:
            os.stat(caminho + nomeArq)
        except:
            arquivo = open(caminho + nomeArq, 'w')
            arquivo.write("0")
            arquivo.close()