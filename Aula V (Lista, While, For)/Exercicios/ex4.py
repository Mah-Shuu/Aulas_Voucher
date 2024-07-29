# Faça um algoritmo que receba o número de avaliações do estudante que será (utilizado como contador),
# após receba as notas e apresente a média do estudante.

contador=int(input("Digite a quantidade de avaliações de um estudante: "))
avaliacoes=[]
i=0
while i<contador:
    i+=1
    avaliacoes.append(float(input("Digite a nota da avaliação: ")))
media=sum(avaliacoes)/contador
print(f"Média: {media:.2f}")

#--------------------------------------------

# numero_avaliacoes = int(input("Digite o numero de provas: "))
# i=0
# soma=0
# while i<numero_avaliacoes:
#     soma+=float(input("Digite a nota: "))
#     i+=1

# media= soma / numero_avaliacoes
# print(media)