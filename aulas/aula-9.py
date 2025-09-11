'''lista = []

i = 0

while i in range(3):
    convidado = input('informe o nome do convidado: ')
    lista.append(convidado)

    i += 1


for x, z in enumerate(lista):
    print(f'{x + 1} - {z}')'''


'''def mostrar_carrinho(lista):

    if not lista:
        print('Seu carrinho está vazio')
        return

    print('\n === Itens no carrinho: ===\n')
    for x, z in enumerate(lista):
        print(f'{x + 1} - {z}')

def mostrar_menu():
        print('\n=== Menu ===\n')
        print('1 - Adicionar produto\n')
        print('2 - Ver carrinho\n')
        print('3 - Sair\n')
        
carrinho = []

while True:

    mostrar_menu()

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        produto = input('\nInforme o produto: ')
        carrinho.append(produto)
        print(f'\nProduto {produto} adicionado ao carrinho.\n')
       
    elif escolha == '2':
       mostrar_carrinho(carrinho)
    
    elif escolha == '3':
         print('Encerrando o programa.')
         break
    else:
        print('Opção inválida. Tente novamente.\n')'''


biblioteca = []

def mostrar_menu():
        print('\n=== Menu ===\n')
        print('1 - Adicionar livro\n')
        print('2 - Ver quantidade de livros cadastrados\n')
        print('3 - Ver biblioteca completa\n')
        print('4 - Mudar livros de posição?\n')
        print('5 - Verificar Livro\n')
        print('6 - Sair\n')

def adicionar_livro(livro):
    biblioteca.append(livro)
    print(f'\nLivro {livro} adicionado a biblioteca.\n')

def quant_livros():
    print(f'\nQuantidade de livros cadastrados: {len(biblioteca)}\n')

def ver_biblioteca():
    if not biblioteca:
        print('Sua biblioteca está vazia')
        return

    print('\n === Livros na biblioteca: ===\n')
    for x, z in enumerate(biblioteca):
        print(f'{x + 1} - {z}')

def mudar_posicao(pos1, pos2):
    if pos1 < 1 or pos2 < 1 or pos1 > len(biblioteca) or pos2 > len(biblioteca):
        print('Posições inválidas. Tente novamente.\n')
        return

    biblioteca[pos1 - 1], biblioteca[pos2 - 1] = biblioteca[pos2 - 1], biblioteca[pos1 - 1]
    print(f'Livros nas  {biblioteca[pos1 - 1]} e {biblioteca[pos2 - 1]} foram trocados.\n')

def verificar_livro(livro):
    if livro in biblioteca:
        print(f'O livro "{livro}" está na biblioteca.\n')
    else:
        print(f'O livro "{livro}" não foi encontrado na biblioteca.\n')

while True:

    mostrar_menu()

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        livro = input('\nInforme o nome do livro: ')
        adicionar_livro(livro)
       
    elif escolha == '2':
       quant_livros()
    
    elif escolha == '3':
         ver_biblioteca()
    
    elif escolha == '4':
        try:
            pos1 = int(input('Informe o livro a ser trocado: '))
            pos2 = int(input('Informe a nova posição do livro a ser trocado: '))
            mudar_posicao(pos1, pos2)
        except ValueError:
            print('Por favor, insira números válidos para as posições.\n')
    
    elif escolha == '5':
        livro = input('Informe o nome do livro que deseja verificar: ')
        verificar_livro(livro)
    
    elif escolha == '6':
         print('Encerrando o programa.')
         break
    else:
        print('Opção inválida. Tente novamente.\n')