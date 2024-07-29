# Faça um algoritmo que inicialize uma lista de 10 cidade que deseja conhecer e apresente em ordem decrescente (da última para a primeira);


lista=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<10:
    lista[i]=str(input("Digite uma cidade que deseja conhecer: "))
    i+=1

print(sorted(lista,reverse=True))

