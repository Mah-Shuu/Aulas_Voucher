def soma(*args):
    soma = 0
    for num in args:
        soma+=num
    return soma

res = soma(1,2,3,4,5,6)

print(res)