# 10 – Uma pessoa está interessada em comprar um carro e deseja fazer um financiamento.
#  Ela tem uma quantia X para dar de entrada, uma taxa de juros é definida pelo banco e
#  a pessoa pode escolher o número de parcelas que deseja financiar. ​
#  Crie uma função que simule um financiamento, levando em consideração o regime de juros compostos.
#  O programa deve solicitar ao usuário o valor do veiculo, o valor da entrada, a taxa de juros
#  e a quantidade de parcelas. Além disso, o programa deve exibir o valor total pago, a quantia
#  dos juros pagos e o valor de cada parcela. O programa deve apresentar as informações de forma
#  clara e objetiva, facilitando a compreensão por parte do usuário.

def financiamento(val_veiculo,val_entrada,tax,parcelas):
    lista_parcel = []
    pos_entrada = val_veiculo-val_entrada
    val_parcelas = pos_entrada/parcelas
    val_tax = val_parcelas


    for parcela in range(parcelas):
        val_tax = val_tax+(val_tax*(tax/100))
        lista_parcel.append(val_tax)

    print(f"\nValor total das parcelas: R$ {sum(lista_parcel):.2f}")
    print(f"Juros total: R$ {(sum(lista_parcel)-pos_entrada):.2f}")
    print(f"Valor das parcelas: R$ {((sum(lista_parcel))/parcelas):.2f}")
    print(f"Valor final: R$ {(sum(lista_parcel))+val_entrada:.2f}\n")

val_veiculo = float(input("Digite o valor do veículo: "))
val_entrada = float(input("Digite o valor de entrada: "))
tax = float(input("Digite o valor da taxa de juros: "))
parcelas = int(input("Digite a quantidades de parcelas: "))

financiamento(val_veiculo,val_entrada,tax,parcelas)