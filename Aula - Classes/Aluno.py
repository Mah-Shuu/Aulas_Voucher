class Aluno:
    def __init__(self,nome,ra,n1:float,n2:float,n3:float,n4:float):
        self.nome = nome
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.media = (n1+n2+n3+n4)/4

    def mostrarSituacao(self):
        if self.media>=7 and self.media<=10:
            return "APROVADO"
        elif self.media>=5 and self.media<7:
            return "EXAME"
        elif self.media<5 and self.media>=0:
            return "REPROVADO"
        else:
            return "MÉDIA INVÁLIDA"
        