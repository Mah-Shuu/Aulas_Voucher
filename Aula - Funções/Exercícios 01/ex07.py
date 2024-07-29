# 7 – Crie uma função que efetue o cálculo do salário e como retorno teremos o valor a ser pago conforme o número de horas trabalhadas.
#  Considere a carga horária de 40h por semana como salário base, caso ultrapasse o limite de 40h, o funcionário deve receber 50% a mais por hora excedente.​

# 35 reais por hora
# salario base 1400

def salario(horas):
    relogio = 0
    salario = 0

    for tempo in range(horas):
        relogio+=1
        if relogio>40:
            salario+=52.5
            continue
        salario+=35

    return salario

horas = int(input("Digite a quantidade de horas trabalhadas: "))
print(f"Salário total: R$ {salario(horas):.2f}")



