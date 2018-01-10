from Fachada.Fachada import *
class Listar(object):
    def gerentes(self):
        
        lista = Fachada().listarTodosGerentes()
        linha = "CPF" + " - "
        linha += "Nome" + " - "
        linha += "PIS" + "\n"
        print linha
        
        for g in lista:
            linha = str(g.getCpf()) + " - "
            linha += str(g.getNome()) + " - "
            linha += str(g.getPis())
            print linha
            
    def funcionarios(self):
        
        lista = Fachada().listarTodosFuncionarios()
        linha = "CPF" + " - "
        linha += "Nome" + " - "
        linha += "PIS" + "\n"
        print linha
        
        for g in lista:
            linha = str(g.getCpf()) + " - "
            linha += str(g.getNome()) + " - "
            linha += str(g.getPis())
            print linha