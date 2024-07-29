# Receba um número inteiro positivo na entrada  e imprima os n 
# primeiros números ímpares naturais. Para a saída, siga o 
# formato do exemplo abaixo.

# Exemplo:
# Digite o valor de n: 5
# 1
# 3
# 5
# 7
# 9

# contador = int(input("Digite o valor de n: "))
# v=0
# i=0
      
# while not v==contador:
#     i+=1
#     if i%2==0:
#         continue
#     else:
#         print(i)
#         v+=1

#--------------------------------------------

num = int(input("Digite o valor de n: "))
cont=0
i=1
      
while cont<num:
    
    print(i)
    i+=2
    cont+=1