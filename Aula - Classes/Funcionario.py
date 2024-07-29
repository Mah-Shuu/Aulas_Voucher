class Funcionario:
    def __init__(self,nome:str,sobrenome:str,horasTrabalhadas:int,valorHora:float):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horasTrabalhadas = horasTrabalhadas
        self.valHora = valorHora

    def nomeCompleto(self):
        return f"{self.nome} {self.sobrenome}"
    
    def calcularSalario(self):
        return f"Salário: {(self.horasTrabalhadas*self.valHora):.2f}"
    
    def incremetentarHoras(self,horas):
        self.horasTrabalhadas+=horas
        

        