class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def getNome(self):
        print(f"Nome: {self.nome}")

    def getIdade(self):
        print(f"Idade: {self.idade}")

    def getMatricula(self):
        print(f"Matrícula: {self.matricula}")

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade,formacao,disciplina,ch,sal):
        super().__init__(matricula, nome, idade)
        self.form = formacao
        self.disp = disciplina
        self.ch = ch
        self.salario = sal

    def lecionar(self):
        print(f"Prof. {self.nome} está lecionando...")

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade,*notas):
        super().__init__(matricula, nome, idade)
        self.notas = []
        for nota in notas:
            self.notas.append(nota)
        self.media = (sum(self.notas)/(len(self.notas)))

    def getMedia(self):
        print(f"Média: {self.media}")


aluno1 = Aluno(1214,"Pedro",17,10,6,4,6,7.5)
professor1 = Professor(2356,"Roberto",31,"Top","Matemática",4,2600)

print()

aluno1.getMedia()
aluno1.getNome()
professor1.lecionar()