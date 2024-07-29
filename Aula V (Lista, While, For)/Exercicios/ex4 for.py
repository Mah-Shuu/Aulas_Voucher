num_notas=int(input("Digite o numero de avaliações: "))
provas=[]
for nota in range(num_notas):
    provas.append(float(input("Digite a nota: ")))

media=sum(provas)/num_notas
print(media)