# CONTADOR DE CARACTERES EM STRING

'''

nome = "suzane"
print(f'O nome tem {len(nome)} letras.')

for i in range(len(nome)):
    print(f'{i+1}ª letra: {nome[i]}')

'''

# CONTADOR PARA NUMEROS PARES DE 0 A 50

'''

for i in range(0, 51, 2):
    print(i)
    
 

for i in range(1, 51):
    
    if i % 2  == 0:
        
        print(i)

'''

# TABUADA SOMA DE 0 A 10

'''

tabuada = int(input('QUAL TABUADA SERÁ IMPRESSA? '))

for i in range(0, 11, 1):

    print(f'{tabuada} + {i} = {tabuada + i}')

'''

# TABUADA DETERMINANDO O NÚMERO E A OPERAÇÃO

'''

tab = int(input('QUAL A TABUADA SERÁ IMPRESSA? '))

operacao = input('QUAL A OPERAÇÃO? (+, -, *, /) ')

for i in range(0, 11):
    if operacao == "+":
        
        print('{} {} {} = {}'.format(tab, operacao, i, tab + i))
    
    elif operacao == "-":
        
        print('{} {} {} = {}'.format(tab, operacao, i, tab - i))
    
    elif operacao == "*":
        
        print('{} {} {} = {}'.format(tab, operacao, i, tab * i))
    
    else:
        if i == 0:
            print('{} {} {} = INDETERMINADO'.format(tab, operacao, i))
        
        else:
            print('{} {} {} = {}'.format(tab, operacao, i, round(tab / i, 2)))

'''

# CONTAGEM DE TEMPO

'''

from time import sleep

for time in range(10, 0, -1):
    print(time)
    sleep(1)

print('BOOOOM')

'''

# IMPRIMIR NOMES DE LISTA EM MAIÚSCULO

'''

nomes = ["Alice", "Bob", "Charlie", "David", "Eve"]

for nome in nomes:
 
    print(nome.upper())

'''

# SOMA DOS VALORES DE 1 A 100

soma = 0

for i in range(1, 101):
    soma = soma + i

print(f' A SOMA DOS NÚMEROS DE 1 A 100 É: {soma}')