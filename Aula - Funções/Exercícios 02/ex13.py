def criaLista(quant: int,valor: str):
    lista = []
    for vezes in range(quant):
        lista.append(valor)
    return lista

lista = criaLista(5,"x")
print(lista)