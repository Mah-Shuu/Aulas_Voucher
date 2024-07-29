class Pessoa:
    def __init__(self,nome,tel,email,ender):
        self.nome = nome
        self.tel = tel
        self.email = email
        self.ender = ender

    def negociar(self):
        print(f"{self.nome} quer comprar a casa do Krebin du gral")

class Física(Pessoa):
    def __init__(self, nome, tel, email, ender,cpf):
        super().__init__(nome, tel, email, ender)
        self.cpf = cpf

    def tomarAgua(self,quant):
        print(f"{self.nome} bebeu {quant} ml de água")


class Jurídica(Pessoa):
    def __init__(self, nome, tel, email, ender, cnpj):
        super().__init__(nome, tel, email, ender)
        self.cnpj = cnpj

    def processar(self,quem):
        print(f"{self.nome} no CNPJ {self.cnpj} processou {quem}")

pessoa1 = Jurídica("Clabinho do Grau","67 12345678910","clebindograu@gmail.com","Rua Tchurusbango Tchurusbargos","10142dois4066")
pessoa2 = Física("Augustinho Carrara","67 6666-6666","augustaodasvariassilvas@gmail.com","Casa da mae joana",69696969)


pessoa1.processar("Carlão da Rebolagi")
pessoa2.tomarAgua(2000)
pessoa1.negociar()