# MEDIA

def media(n1, n2, n3, nome):
    media = round((n1 + n2 + n3) / 3, 2)
    print(f" {nome}, SUA MÉDIA: {media}")


# nome = input("INFORME SEU NOME: ")
# n1 = float(input("NOTA 1: "))
# n2 = float(input("NOTA 2: "))
# n3 = float(input("NOTA 3: "))

# media(n1, n2, n3, nome)

# OPERADORES

def operadores(numero_1, numero_2):
    print(f'SOMA: {numero_1} + {numero_2} = ',numero_1 + numero_2)
    print(f'SUBTRAÇÃO: {numero_1} - {numero_2} = ',numero_1 - numero_2)
    print(f'MULTIPLICAÇÃO: {numero_1} * {numero_2} = ',numero_1 * numero_2)
    print(f'DIVISÃO: {numero_1} / {numero_2} = ',numero_1 / numero_2)
    print(f'RESTO DA DIVISAO: {numero_1} % {numero_2} = ',numero_1 % numero_2)
    print(f'POTÊNCIA: {numero_1} ^ {numero_2} = ',numero_1 ** numero_2)

x = int(input('INFORME UM NÚMERO: '))
# y= int(input('INFORME OUTRO NÚMERO: '))

# operadores(x, y)

# COMPARADORES

def comparadores(a, b):
    
    if a != b:
        print(f'{a} é diferente de {b}')

    if a > b:
        print (f'{a} é maior que {b}')
    elif a < b:
        print(f'{a} é menor que {b}')
    else:
        print('OS NÚMEROS SÃO IGUAIS')
        
# comparadores(x, y)

# print(f'O NÚMERO {x} TEM:\nANTECESSOR: {x - 1}\nSUCESSOR: {x + 1}')

# print(f'Z = {(x**2 + y**2)/(x-y)**2}')

reajuste = 0.35

print(f'O SALÁRIO INICIAL ERA {x}\nO REAJUSTE FOI DE {reajuste * 100}% E O SALÁRIO FINAL É DE {x * reajuste + x}')
