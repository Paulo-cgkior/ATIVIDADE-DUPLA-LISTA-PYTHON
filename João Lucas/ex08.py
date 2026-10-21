import os
os.system("cls")

vetor_nome = []
vetor_salario = []
contador_2000 = 0

for i in range(5):
    nome = str(input(f'Digite o {i+1} nome: '))
    vetor_nome.append(nome)
    salario = float(input('Digite seu salário: '))
    vetor_salario.append(salario)
    if salario >= 2000:
        contador_2000 += 1
max_salario = max(vetor_salario)
posicao = vetor_salario.index(max_salario)

os.system("cls")
print(f'Nome de quem tem o maior salário: {vetor_nome[posicao]} ')
print(f'Maior salário: R$ {max_salario}')
print(f'Quantos ganham acima de 2000: {contador_2000}')