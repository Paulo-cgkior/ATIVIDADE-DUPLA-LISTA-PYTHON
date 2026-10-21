import os
os.system("cls")

numero = 0
soma = 0
contadordez = 0
numero_vet = []

for i in range(10):
    numero = float(input(f"Digite seu {i+1}º número: "))
    numero_vet.append(numero)
    soma += numero
    if numero > 10:
        contadordez += 1

print(f"Soma: {soma}")
print(f"Quantidade de numeros maiores que dez: {contadordez}")