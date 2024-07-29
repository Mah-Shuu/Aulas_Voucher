# 2 – Crie uma função para calcular a exponenciação, que necessite dois argumentos e apresente como resultado a potência. Sendo base elevado ao expoente.​

def expo(n1,n2):
    expo = n1**n2
    return expo

n1=int(input("Digite a base: "))
n2=int(input("Digite o expoente: "))
print(expo(n1,n2))