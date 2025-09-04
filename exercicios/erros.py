# problema 1

'''

notas = (7, 8, 9)

if notas > 7: # o erro foi comparar a tupla com um inteiro
    print("Aprovado")

    '''

# solucao correta

notas = (7, 8, 9)

soma = sum(notas) / len(notas)

if soma > 7:
    print("Aprovado")

# problema 2

'''

cidades = ("São Luis", "Teresina", "Fortaleza")

for i in range(cidades): # o erro foi tentar usar uma tupla como inteiro
    print(cidades[i])

    '''

# solucao correta

cidades = ("São Luis", "Teresina", "Fortaleza")

for cidade in cidades:
    print(cidade)

# problema 3

'''

pares = (2, 4, 6, 8)
i = 0

while i < pares: # o erro foi tentar comparar um inteiro com uma tupla
    print(pares[i])
    i += 1
    
'''

# solucao correta

pares = (2, 4, 6, 8)

print("Números pares:", len(pares))


# problema 4

'''

nomes = () # tupla vazia. nunca haverá nomes cadastrados

if nomes:
    print('lista de nomes encontrada')
else:
    print('sem nomes cadastrados')
    
'''

# solucao correta

nomes = ('Ana', 'João', 'Carlos') # tupla com nomes cadastrados
if nomes:
    print('lista de nomes encontrada')
else:
    print('sem nomes cadastrados')


# problema 5

'''

dados = ('joão', 20, 'masculino')

for dado in dados:
    if dado.append('aluno'): # o erro foi tentar usar o metodo append em uma tupla
        print(dado)
        
'''

# solucao correta

dados = ('joão', 20, 'masculino')
lista_dados = list(dados)  # converter a tupla em lista
lista_dados.append('aluno')  # agora é possível usar o append
for dado in lista_dados:
    print(dado)

# problema 6

'''nomes = ('ana', 'joao', 'carlos')

if "maria" in nomes[0]: # o erro foi tentar acessar um índice específico sem necessidade
    print("maria encontrada")

'''

# solucao correta

nomes = ('ana', 'joao', 'carlos')

if "maria" in nomes:
    print("maria encontrada")
else:
    print("maria não encontrada")


# problema 7

idades = (15, 18, 21, 30)

'''

for idade in idades:
    if idades >= 18: # o erro foi comparar a tupla com um inteiro
        print("maior de idade: ", idade)

'''

# solucao correta

idades = (15, 18, 21, 30)
for idade in idades:
    if idade >= 18:
        print("maior de idade: ", idade)

# problema 8

'''

valores = (10, 20, 30)

i = 0

while i < len(valores):
    if valores[i] > 15: # o erro foi comparar o mesmo valor da tupla com um inteiro. isso causa um loop infinito, já que o valor nunca é alterado
        print('maior que 15: ', valores[i])

        
'''

# solucao correta

valores = (10, 20, 30)

for valor in valores:
    if valor > 15:
        print('maior que 15: ', valor)


# problema 9

'''

cores = ("azul", "verde", "amarelo")

for cor in cores:
    if cor == "verde":
        cores[1] = "vermelho" # o erro está em tentar alterar o valor de uma tupla que é imutável

'''

# solucao correta

cores = ("azul", "verde", "amarelo")

lista_cores = list(cores)  # converter a tupla em lista

for i in range(len(lista_cores)):
    if lista_cores[i] == "verde":
        lista_cores[i] = "vermelho"  # agora é possível alterar o valor

print(lista_cores)


# problema 10

'''

numeros = (1, 2, 3)

for i in range(4):
    print(numeros[i]) # o erro foi tentar acessar um índice que não existe na tupla (numeros[4])

'''

# solucao correta

numeros = (1, 2, 3)

for i in range(len(numeros)):
    print("índice", i, ":", numeros[i])