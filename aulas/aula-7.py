# TUPLAS

alunos = ('davi', 'ana claudia', 'magno', 'luis', 'roberta', 'rian')

for aluno in alunos:
    print(f'{alunos.index(aluno)}: {aluno.capitalize()}')

print(alunos.index('luis', 2, 5))

print(alunos[:3])

num = (1, 2, 3, 4, 5, 6 ,7)

print(num*3)

i = 0

for nome in alunos:
    print(i, nome)
    i += 1

for indice, nome in enumerate(alunos, start = 1):
    print(indice, nome)


num = (1, 2, 3, 4, 5)
nomes = ('davi', 'ana claudia', 'magno', 'luis', 'roberta', 'rian')

print(f'\no tamanho da tupla num é: {len(num)}')

print(f'\nnomes em ordem alfabética: {sorted(nomes)}\n')



num = (1, 3, 545, 2, 23, 52, 87, 45, 34, 12, 100, 4)

print('os números ímpares sorteados são:', end="")
for numero in sorted(num):
    if numero % 2 != 0:
        print(f' {numero}', end=" ")
print('\n')


valores = []

while len(valores) != 6:
    valor = int(input(' digite um valor: '))

    valores.append(valor)

numeros = tuple(valores)

print(f'\nValores: {numeros}\n')

numero = int(input('qual valor deseja checar? '))

if numero in numeros:
    print(f'\no número {numero} aparece {numeros.count(numero)} vez(es)')

else:
    print(f'\no número {numero} não aparece na tupla')

pares = []

for num in numeros:

    if num % 2 == 0:
        pares.append(num)

print(f'\nos números pares da tupla são: {pares}\n')
