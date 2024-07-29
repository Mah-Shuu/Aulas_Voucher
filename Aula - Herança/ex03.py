class Ingresso:
    def __init__(self,preco:float,setor:str):
        self.preco = preco
        self.setor = setor

    def alterarPreco(self,novoPreco):
        if novoPreco>0:
            self.preco = novoPreco
            print("Preço alterado.")
        else:
            print("Valor inválido")

    def mostrarSetor(self):
        print(f"Setor: {self.setor}")

class IngressoVIP(Ingresso):
    def __init__(self, preco:float, setor:str,camarote:bool,openBar:bool,openFood:bool,estacionamento:bool):
        super().__init__(preco, setor)
        self.cam = camarote
        self.ob = openBar
        self.of = openFood
        self.est = estacionamento

    def pegarBebida(self):
        if self.ob == True:
            print("Você pode pegar uma bebida.")
        else:
            print("Você não pode pegar uma bebida.")

    def acessarCamarote(self):
        if self.cam == True:
            print("Acessou o camarote.")
        else:
            print("Não pode acessar o camarote")

ingresso1 = Ingresso(24.99,"Sala A")
ingresovip1 = IngressoVIP(99.99,"Sala VIP",True,True,True,True)
ingresovip2 = IngressoVIP(50.00,"Sala VIP",False,False,True,True)

ingresso1.mostrarSetor()
ingresso1.alterarPreco(29.99)

print()

ingresovip1.acessarCamarote()
ingresovip1.pegarBebida()
ingresovip1.mostrarSetor()

print()

ingresovip2.acessarCamarote()
ingresovip2.pegarBebida()