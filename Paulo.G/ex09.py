import os
os.system("cls")

vetor_antes = []

print("Digite 6 números inteiros:")
for i in range(6):
    num = int(input(f"Número {i + 1}: "))
    vetor_antes.append(num)

vetor_depois = []
for num in vetor_antes:
    if num % 2 == 0:
        vetor_depois.append(0)
    else:
        vetor_depois.append(1)

os.system("cls")

print("\n--- Resultados ---")
print(f"Vetor antes:  {vetor_antes}")
print(f"Vetor depois: {vetor_depois}")
