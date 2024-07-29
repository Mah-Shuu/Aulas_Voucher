quant=int(input("Digite a quantidade de num para o vetor: "))
vet1=[]
vet2=[]

for i in range(quant):
    num=int(input("Digite um número: "))
    vet1.append(num)
    vet2.append(num*5)

print(vet1)
print(vet2)