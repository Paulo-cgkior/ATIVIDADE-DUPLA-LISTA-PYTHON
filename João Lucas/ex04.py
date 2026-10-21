import os
os.system("cls")

vetor_num = []

for i in range(8):
    num = int(input(f'Digite o {i + 1}º número: '))
    vetor_num.append(num)

os.system('cls')
num_escolhido = int(input(f'Digite o número a ser pesquisado: '))
if num_escolhido in vetor_num:
    pos = vetor_num.index(num_escolhido)
    print(f'{pos + 1}º número: {num_escolhido}')
else:
    print('Número não encontrado')