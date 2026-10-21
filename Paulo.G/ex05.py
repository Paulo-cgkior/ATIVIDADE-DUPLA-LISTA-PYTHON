import os
os.system("cls")

soma = 0
nota = 0
notas_vet = []
validos_vet = []
QUANTIDADE_DE_NOTAS = 5

for i in range(QUANTIDADE_DE_NOTAS):
    nota = float(input("Digite seu número: "))
    if nota >= 7:
        validos_vet.append(nota)
    notas_vet.append(nota)
    soma += nota

media = soma / QUANTIDADE_DE_NOTAS

print(f"Notas: {notas_vet}")
print(f"Media: {media}")
print(f"Validos: {validos_vet}")