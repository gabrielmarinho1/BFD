'''

while True:
    resposta = input("DIGITE 'SAIR' PARA ENCERRAR: ")

    if resposta.upper() == "SAIR":
        print('FUI!')

        break

 '''

'''

while True:
    estado = input('INFORME SEU ESTADO CIVIL: (SOLTEIRO/CASADO) ').upper()

    if estado == "SOLTEIRO" or estado == 'CASADO':
        break

'''

'''

print('BEM VINDO AOS SERVIÇOS NU')
senha = 'python123'
tentativa = input('DIGITE A SENHA: ').lower()

if tentativa == senha: 

    print('ACESSO PERMITIDO')

else:
    erros = 1

    while tentativa!= senha:

        print('SENHA INCORRETA. TENTE NOVAMENTE.')
        print(f'VOCÊ AINDA TEM {3 - erros} TENTATIVA(S)')

        tentativa = input('DIGITE A SENHA: ').lower()

        erros += 1

        if erros > 2:
            print('ACESSO BLOQUEADO')
            break

'''

'''

aluno = input('QUAL O SEU NOME? ')

while aluno != 'fim':
    minutos = int(input('QUANTOS MINUTOS VOCÊ CONSEGUE ESPERAR ATÉ A MERENDA? '))

    if minutos < 5:
        print(aluno + ' está com muita fome" pode pegar o lanche agora!')
    
    elif minutos >= 5 and minutos <= 15:
        print(aluno + ' ainda pode esperar mais um pouco')
    
    else:
        print(aluno + ' pode brincar mais antes da merenda')

'''

'''

numero = int(input('digite um número: '))

soma = 0

while numero != 0:
    soma += numero
    numero = int(input('digite um número: '))

    
print(f'\na soma dos números é: {soma}\n')

'''


regular = 0
bom  = 0
excelente = 0
expectadores = 1

while expectadores <= 8:
    print(f'\nexpectador {expectadores} de 20\n')
    idade = int(input('qual sua idade? '))
    expectadores += 1
    
    opniao = int(input('qual sua opnião sobre o filme? (1 - regular; 2 - bom; 3 - excelente) '))

    if opniao == 1:
        regular += 1

    elif opniao == 2:
        bom += 1

    elif opniao == 3:
        excelente += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

print('\n--- resultado da pesquisa---\n')
print(f'regular: {regular}')
print(f'bom: {bom}')
print(f'excelente: {excelente}')

