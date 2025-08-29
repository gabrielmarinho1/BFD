'''

original = float(input('DIGITE O PREÇO ORIGINAL DO PRODUTO: '))

desconto = original * .20

final = original - desconto

print(f'O PREÇO ORIGINAL DO PRODUTO ERA R$ {original:.2f}. O DESCONTO FOI DE R$ {desconto:.2f} E O PREÇO FINAL É R$ {final:.2f}')

'''

'''
import random

sorte = random.randint(1, 1000)

numero = int(input('TENTE A SORTE COM UM NÚMERO DE 1 A 1000! DIGITE SEU NÚMERO: '))

if numero == sorte:
    print(f'CERTO!! O NÚMERO DA SORTE É {sorte}')
else:
    print(f'ERRADO! O NÚMERO DA SORTE É {sorte}, NÃO {numero}')
    
'''

'''
num = int(input('DIGITE UM NÚMERO: '))

if num % 2 == 0:
    
    print(f'O NÚMERO {num} É PAR.')

else:
    
    print(f'O NÚMERO {num} É ÍMPAR')
    
'''    

'''
    
time = input('INFORME O NOME DO TIME: ')

if time == 'time':
    print('MELHOR DO MUNDO!')
else:
    print('SOFREDOR ETERNO!')
    
'''

'''
n = float(input('DIGITE UM NÚMERO: '))

if n > 0:
    print(f'O NÚMERO {n} É POSITIVO')
elif n < 0:
    print(f'O NÚMERO {n} É NEGATIVO')
else:
    print('O NÚMERO É 0')

'''

'''
rodas = int(input('DIGITE O NÚMERO DE RODAS DO VEÍCULO: '))


if rodas == 2:
    print('BICICLETA OU MOTO')
elif rodas == 3:
    print('TRICICLO OU UM TUK-TUK')
elif rodas == 4:
    print('PROVAVELMENTE UM CARRO')
elif rodas == 6:
    print('PODE SER UM CAMINHÃO PEQUENO')
elif rodas >= 8 and rodas <= 16:
    print('CAMINHÃO GRANDE OU ÔNIBUS')
else:
    print('VEÍCULO DESCONHECIDO')


'''


if input("VOCÊ VAI PARA O FESTEJO DE SÃO BENEDITO? ").lower() == "sim":
    if int(input('QUE HORAS? ')) < 23:
        print('PARTIU MISSA!!')
    else:
        print('PARTIU SERESTA!!')
else:
    print('BOAS AVE MARIAS FAZ, QUEM EM SUA CASA ESTÁ EM PAZ.')











    