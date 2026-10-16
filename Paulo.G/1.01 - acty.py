import os
os.system("cls")

num = 0
num_vet = []

for i in range(5):
    num = int(input(f"Digite seu {i+1}º número: "))
    num_vet.append(num)

print("")

for i, num in enumerate(num_vet, start=1):
    print(f"{i + 1}º número: {num}")

print("")

for i,num in enumerate(reversed(num_vet)):
    print(f"{i - 1}º número: {num}")