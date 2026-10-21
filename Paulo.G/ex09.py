import os
os.system("cls")

num = 0
num_vet = []
impar_vet = []
par_vet = []
impar_um = []
par_zero = []

for i in range(6):
    num = int(input(f"Digite seu {i+1}º numero: "))
    if num % 2 == 1:
        par_vet.append(num)
        par_zero.append(num)
    else:
        impar_vet.append(num)
        impar_um.append(num)
    num_vet.append(num)


print(f"Vetor: {num_vet}")
print(f"Vetor: {impar_vet}")
print(f"Vetor: {par_vet}")

impar_um = 1
par_zero = 0
print(f"Vetor: {num_vet}")
print(f"Vetor: {impar_um}")
print(f"Vetor: {par_zero}")