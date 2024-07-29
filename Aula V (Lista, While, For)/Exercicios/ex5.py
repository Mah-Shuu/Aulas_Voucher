# Crie um programa que receba a palavra
# FELICIDADE  e imprima a posição de cada letra da
# palvra e iforme qual letra está sendo impressa
# na posição x. Após imprima a mensagem que o 
# programa doi finalizado. Exemplo: 

# Posição 0 da Lista: F
# Posição 1 da Lista: E
# Posição 2 da Lista: L
# Posição 3 da Lista: I
# Posição 4 da Lista: C
# Posição 5 da Lista: I
# Posição 6 da Lista: D
# Posição 7 da Lista: A
# Posição 8 da Lista: D
# Posição 9 da Lista: E
# Programa finalizado.

felicidade="FELICIDADE"
cont=0
for letra in felicidade:
    print("Posição ",cont," da Lista: ",letra)
    cont+=1
print("Programa finalizado.")