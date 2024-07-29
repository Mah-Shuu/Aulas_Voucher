# 4 – Escreva um programa, com uma função que necessite de um argumento.
#  A função retornar o valor de caractere ‘P’, se seu argumento for positivo, e
#  ‘N’, se seu argumento for zero ou negativo.​

def ver_valor (num):

    if num<=0:
        return "N"
    else:
        return "P"
    
num = int(input("Digite um número: "))
print(ver_valor(num))
