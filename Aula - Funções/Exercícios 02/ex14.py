def kwh (p,t):
    total = (p*t)/1000
    return total

def consumo(kwh):
    total = kwh*30
    return total

potencia = kwh(4500,0.5)
consumoTotal = consumo(potencia)    

print(consumoTotal)