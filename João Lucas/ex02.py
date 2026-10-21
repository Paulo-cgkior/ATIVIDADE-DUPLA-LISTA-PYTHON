import os
os.system("cls")

vetor_temp = []
max_temp = 0
min_temp = 0
temp_unit = 0

for i in range(7):
    temp = int(input(f'Digite a temperatura do {i + 1}º dia da semana em C°: '))
    vetor_temp.append(temp)
    temp_unit = temp_unit + 1
    if temp_unit == 1:
        max_temp = temp
        min_temp = temp
    else:
        max_temp = max(max_temp, temp)
        min_temp = min(min_temp, temp)

os.system('cls')
media = sum(vetor_temp) / 7
for i, temp in enumerate(vetor_temp):
    print(f'Temperatura do {i + 1}º dia da semana: {temp}')
print(f'Média: {media}')
print(f'Maior Temperatura: {max_temp}')
print(f'Menor Temperatura: {min_temp}')