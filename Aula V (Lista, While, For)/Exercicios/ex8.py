# Faça para 10 números inteiros para um vetor de inteiros. Computar um seundo vetor
# que terá o resultado da multiplicação por um escalar inteiro 5.
quant=int(input("Digite a quantidade de num para o vetor: "))
vet1=[]
vet2=[]
i=0
while i<quant:
    num=int(input("Digite um número: "))
    vet1.append(num)
    vet2.append(num*5)
    i+=1

print(vet1)
print(vet2)