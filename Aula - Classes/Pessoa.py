class Pessoa:

    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def getNome(self):
        return self.nome
    
    def setIdade(self,novaIdade):
        self.idade = novaIdade

    def getEndereco(self):
        return self.endereco
