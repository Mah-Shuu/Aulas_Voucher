class Filme:
    def __init__(self,nome,duração):
        self.nome = nome
        self.duracao = duração

    def play(self):
        print(f"O seguinte filme está sendo reproduzido: {self.nome}")

class Ação(Filme):
    def __init__(self, nome, duração):
        super().__init__(nome, duração)

    def explosao(self):
        print("BOOOOOOM!!!")

        
class Drama(Filme):
    def __init__(self, nome, duração):
        super().__init__(nome, duração)
    
    def choro(self):
        print(";-; mt triste")

class Comédia(Filme):
    def __init__(self, nome, duração):
        super().__init__(nome, duração)
    
    def rir(self):
        print("XD mt funny esse filme")
    
filmeAcao = Ação("Os Tchakablaka",600000000)
filmeDrama = Drama("Amores Trsites Demais",180)
filmeComedia = Comédia("Os Bunga Lau",240)

print()

filmeAcao.play()
filmeAcao.explosao()

print()

filmeDrama.play()
filmeDrama.choro()

print()

filmeComedia.play()
filmeComedia.rir()

print()