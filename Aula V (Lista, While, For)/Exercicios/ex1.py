# Faça um algoritmo que receba um número e apresente a cont do mesmo ao final;

num=int(input("Digite um número: "))
cont = 0 #CONTADOR (CONTROLE DO WHILE)
while cont<10:
    cont +=1
    print(num," x ",cont," = ",num*cont)
