import os
os.system("cls")

num = 0
contador = 0
num_vet = []
positivos_vet = []
QUANTIDADE_DE_NOTAS = 5

for i in range(QUANTIDADE_DE_NOTAS):
    num = int(input("Digite seu número: "))
    if num >= 0:
        positivos_vet.append(num)
        contador += 1
    num_vet.append(num)

print(f"Positivos: {contador}")
print(f"Notas: {num_vet}")
print(f"Positos: {positivos_vet}")