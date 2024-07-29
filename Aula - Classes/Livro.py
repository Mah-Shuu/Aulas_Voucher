class Livro:
    def __init__(self,nome,autor,editora,pag):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.pag = pag

    def setEditora(self,novaEditora):
        self.editora = novaEditora

    def getPag(self):
        for pag in range(self.pag):
            print(pag)
        