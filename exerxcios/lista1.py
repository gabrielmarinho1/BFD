# QUESTÃO 1

vitorias = 0
empates = 0
derrotas = 0

for jogo in range(0, 5):
    selecao = int(input(f"GOLS DA SELEÇÃO NO JOGO {jogo + 1}: "))

    adversario = int(input(f"GOLS DO ADVERSÁRIO NO JOGO {jogo + 1}: "))
    print('\n')

    if selecao == adversario:
        empates += 1
    elif selecao > adversario:
        vitorias += 1
    else:
        derrotas += 1

print("=== TORNEIRO DE FUTEBOL ===")
print(f'VITÓRIAS: {vitorias}')
print(f'EMPATES: {empates}')
print(f'DERROTAS: {derrotas}')
print("\n")

# QUESTÃO 2


import random

secreto = random.randint(1, 20)
acerto = False

for i in range(0, 5):
    tentativa = int(input('ADVINHE O NÚMERO (1 A 20): '))
    if tentativa == secreto:
        print("VOCÊ ACERTOU!")
        acerto = True
        break
    elif tentativa < secreto:
        print("MUITO BAIXO!")
    else:
        print('MUITO ALTO')

if acerto == False:
    print(f"GAME OVER! O NÚMERO ERA {secreto}")

print("\n")

# QUESTÃO 3


pessoas = int(input('QUANTAS PESSOAS VÃO AO SHOW? '))

total = 0

for pessoa in range(0, pessoas):
    idade = int(input(f'\nIDADE DA PESSOA {pessoa + 1}: '))
    if idade <= 12:
        print("\nENTRADA GRÁTIS")
    
    elif idade >=13 and idade < 17:
        print("\nMEIA ENTRADA (R$ 10)")
        total += 10
    else:
        print("\nINGRESSO INTEIRO (R$ 20)")
        total += 20

print(f'\nTOTAL ARRECADADO: R$ {total}\n')

# QUESTÃO 4


print('=== QUIZ DE CONHECIMENTOS GERAIS ===\n')

perguntas = ["CAPITAL DO BRASIL? ", "PLANETA CONHECIDO COMO PLANETA VERMELHO? ", "QUEM ESCREVEU DOM QUIXOTE? ", "QUAL O MAIOR OEANO? ", "QUAL A COR DA CLOROFILA? "]
alternativas = [["SÃO PAULO", "BRASÍLIA", "RIO DE JANEIRO"], ["MARTE", "JÚPITER", "VÊNUS"], ["MACHADO DE ASSIS", "CERVANTES", "SHEAKSPEARE"], ["ATLÂNTICO", "PACÍFCO", "ÍNDICO"], ["VERDE", "AZUL", "AMARELA"]]
respostas = [2, 1, 2, 2, 1]
acertos = 0

for pergunta in perguntas:
    index = perguntas.index(pergunta)
    print(f'\n{index + 1}) {pergunta}\n')
    
    print(f'1 - {alternativas[index][0]}')
    print(f'2 - {alternativas[index][1]}')
    print(f'3 - {alternativas[index][2]}\n')

    resposta = int(input("SUA RESPOSTA: "))
    
    if resposta == respostas[index]:
        acertos +=1

print(f"\nPONTUAÇÃO FINAL: {acertos}/5")

if acertos == 5:
    print("\nGÊNIO!!\n")
elif acertos == 3 or acertos == 4:
    print("\nMANDOU BEM!\n")
elif acertos == 1 or acertos == 2:
    print('\nPRECISA ESTUDAR MAIS\n')
else:
    print('\nZEROU O QUIZ\n')


# QUESTÃO 5

candidatos = [0, 0, 0]


for avaliador in range(0, 3):
    candidatos[0] += int(input(f'NOTA DO AVALIADOR {avaliador + 1} PARA O CANDIDATO 1: '))
    candidatos[1] += int(input(f'NOTA DO AVALIADOR {avaliador + 1} PARA O CANDIDATO 2: '))
    candidatos[2] += int(input(f'NOTA DO AVALIADOR {avaliador + 1} PARA O CANDIDATO 3: '))
    print('\n')

print("=== PONTUAÇÃO FINAL ===")

print(f"Candidato 1: {candidatos[0]}")
print(f"Candidato 2: {candidatos[1]}")
print(f"Candidato 3: {candidatos[2]}")

candidatos = list(dict.fromkeys(candidatos))

if len(candidatos) != 3:
    print('\nEMPATE! DISPUTA ACIRRADA\n')

else:
    for candidato in candidatos:
        if candidato == max(candidatos):
            print(f'\nCANDIDATO {candidatos.index(candidato) + 1} É O CAMPEÃO\n')



# QUESTÃO 6

nome = input("DIGITE O NOME DO ALUNO: ").upper()
nota = float(input("\nDIGITE A NOTA DO ALUNO: "))

if nota >= 7:
    print(f"\n{nome} ESTÁ APROVADO(A)")
elif nota >= 5 and nota < 7:
    print(f'\n{nome} ESTÁ DE REPOSIÇÃO')
else:
    print(f'\n{nome} ESTÁ REPROVADO (A)')
