class Conta:
    def __init__(self,nome:str,cpf:str,num:int,saldo:float):
        self.nome = nome
        self.cpf = cpf
        self.num = num
        self.saldo = saldo

    def depositar(self,quant:float):
        self.saldo+=quant
        print(f"Depositado R${quant:.2f} à conta.")

    def sacar(self,quant:float):
        if self.saldo>0:
            self.saldo-=quant
            print(f"Retirado R${quant:.2f} da conta.")
        else:
            print("Saldo Negativo")

    def imprimirSaldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        