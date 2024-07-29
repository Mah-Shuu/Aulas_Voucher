class Passagem:
    def __init__(self,preco:float,assento:int):
        self.preco = preco
        self.assento = assento

    def alterarPreco(self,novoPreco:float):
        if novoPreco>0:
            self.preco = novoPreco
            print("Preço alterado com sucesso.")
        else:
            print("Preço Inválido")

    def escolherAssento(self):
        assentoNew = input("Digite o assento desejado: ")
        self.assento = assentoNew

class PassagemBus(Passagem):
    def __init__(self, preco: float, assento: int,placa:int,leito:str):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print("Ônibus abastecido.")

    def andar(self):
        print(f"Ônibus {self.placa} saiu do {self.leito}")

class PassagemAviao(Passagem):
    def __init__(self, preco: float, assento: int,portaodeembarque,checkin):
        super().__init__(preco, assento)
        self.portEmbarq = portaodeembarque
        self.checkin = checkin

    def decolar(self):
        print("O avião decolou")