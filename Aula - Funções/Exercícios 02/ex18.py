def desconto(dia:str, **kwargs):
    valor = kwargs["valor"]
    taxa = kwargs["taxa"]
    couvert = kwargs["couvert"]
    if dia == "terça":
        desc = 0.10
    elif dia == "quarta":
        desc = 0.15
    elif dia == "quinta":
        desc = 0.20
    valor_desc = valor - (valor*desc)
    valorTotal = (valor_desc + (valor_desc*taxa))+couvert
    print(f"Conta S/ Taxas: {valor_desc}\nConta C/ Taxas:\n Rodízio: {valor_desc}\n Taxa Serviço: {(valor_desc*taxa):.2f}\n Couvert: {couvert}\n TOTAL R$: {valorTotal:.2f}")

desconto('quinta',valor=99.90,taxa=0.10,couvert=15)
