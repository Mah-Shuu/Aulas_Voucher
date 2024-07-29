# 8 – Um pescador, comprou um PC para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
#  maior que o estabelecido pelo regulamento de pesca do MS (50 Kg) deve pagar uma multa de R$ 4,00 por quilo excedente.
#  O pescador precisa que você crie uma função para ler a quantidade de peixes e calcular o excesso. Gravar na variável
#  excesso a quantidade de quilos além do limite e na variável multa o valor da multa que o pescador deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.​

def multa(peso):

    multa = 0
    kilos = 0
    excesso = 0

    while kilos<peso:
        kilos+=1
        if kilos>50:
            multa+=4
            excesso+=1

    print(f"Quantidade: {peso}Kg\nExcesso: {excesso}\nMulta: R$ {multa:.2f}")

multa(int(input("Digite a quantidade de peixes em quilos: ")))