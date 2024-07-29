# 9 – O gestor de uma rede de shoppings, precisa contratar um sistema para administrar o estacionamento, a principal função do sistema é calcularTempo(). Considere o valor mínimo de R$9,00 por hora e R$ 1,50 por hora adicional. O principal argumento da função é o tempo utilizado em minutos, a função deve retornar o valor total. Caso o usuário fique no estacionamento por menos de 15 minutos, o tempo utilizado não será cobrado.​

def calcularTempo(minutos):
    if minutos<15:
    
        return "Tempo utilizado não será cobrado."

    else:
        valor = 9
        hora_add = 60
        while True:
            if minutos>hora_add:
                valor+=1.5
                hora_add+=60
            else:
                break
        
        pis = (valor*0.033)
        cofins = (valor*0.02)
        icms = (valor*0.17)
        impostos = pis+cofins+icms
        Texto = (f"\nTempo: {minutos/60} Hora(s)\nPIS: R$ {pis:.2f}\nCOFINS: R$ {cofins:.2f}\nICMS: R$ {icms:.2f}\nImpostos: R$ {impostos:.2f}\nTotal: R$ {(valor):.2f}\nTotal c/ Imposto: R${(valor+impostos):.2f}")
        return Texto
    
min=int(input("Digite o tempo utilizado no estacionamento em minutos: "))
print(calcularTempo(min))
