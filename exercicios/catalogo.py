catalogo = {
    "Ação": [
        ["Duro de Matar", 1988],
        ["Mad Max: Estrada da Fúria", 2015],
        ["John Wick", 2014],
        ["Gladiador", 2000],
        ["Velozes e Furiosos", 2001]
    ],
    "Comédia": [
        ["Se Beber, Não Case!", 2009],
        ["O Máskara", 1994],
        ["As Branquelas", 2004],
        ["Superbad", 2007],
        ["Click", 2006]
    ],
    "Drama": [
        ["Forrest Gump", 1994],
        ["O Poderoso Chefão", 1972],
        ["Clube da Luta", 1999],
        ["A Espera de um Milagre", 1999],
        ["Um Sonho de Liberdade", 1994]
    ],
    "Ficção Científica": [
        ["Interestelar", 2014],
        ["Matrix", 1999],
        ["Blade Runner", 1982],
        ["De Volta para o Futuro", 1985],
        ["A Origem", 2010]
    ],
    "Terror": [
        ["O Iluminado", 1980],
        ["Invocação do Mal", 2013],
        ["It: A Coisa", 2017],
        ["Atividade Paranormal", 2007],
        ["Pânico", 1996]
    ],
    "Animação": [
        ["Toy Story", 1995],
        ["Shrek", 2001],
        ["Procurando Nemo", 2003],
        ["O Rei Leão", 1994],
        ["Divertida Mente", 2015]
    ],
    "Romance": [
        ["Titanic", 1997],
        ["Diário de uma Paixão", 2004],
        ["La La Land", 2016],
        ["Como Eu Era Antes de Você", 2016],
        ["Orgulho e Preconceito", 2005]
    ]
}

def adicionar_filme(catalogo):

    while True:
        try:
            genero = input("Digite o gênero do filme: ").title()
            titulo = input("Digite o título do filme: ").title()
            ano = int(input("Digite o ano de lançamento do filme: "))
            
            if genero in catalogo:
                catalogo[genero].append([titulo, ano])
            else:
                catalogo[genero] = [[titulo, ano]]
            print(f'Filme "{titulo}" adicionado ao gênero "{genero}".')
            break
        
        except ValueError:
            print("Inválido. Tente novamente.")

def mostrar_catalogo(catalogo, modo):
    if modo == "gênero":
        print('======= GÊNEROS =======')
        for genero in catalogo:
            print(f'\n======= {genero.title()} =======\n')

            for filme, ano in catalogo[genero]:
                print(f'{filme} {(30 - len(filme)) * ' '} {ano}')
    
    elif modo == "filme":

        ordenado = []
        print('======= FILMES =======')
        for genero, filmes in catalogo.items():
            for filme in filmes:
                ordenado.append((filme[0], filme[1]))
        
        ordenado = sorted(ordenado, key=lambda x: x[0])
        for filme, ano in ordenado:
            print(f'{filme} {(30 - len(filme)) * ' '} {ano}')

def remover_filme(catalogo):

    try:
        mostrar_catalogo(catalogo, "gênero")
        genero = input('De qual gênero deseja remover o filme? ').capitalize()
        if genero not in catalogo:
            print("Gênero não encontrado.")
            return
        filmes = catalogo[genero]
        if not filmes:
            print("Não há filmes nesse gênero.")
            return
        print(f'\n======= {genero} =======\n')
        for filme, ano in filmes:
            print(f'{filme} {(30 - len(filme)) * " "} {ano}')
        escolha = input('Qual filme deseja remover? ').lower()
        for filme in filmes:
            if escolha == filme[0].lower():
                filmes.remove(filme)
                print(f'Filme "{escolha}" removido do gênero "{genero}".')
                return
        print("Filme não encontrado.")
    except ValueError:
        print("Inválido. Tente novamente.")

def buscar_filme(catalogo):
    busca = input("Digite o título do filme que deseja buscar: ").lower()
    encontrados = []
    for genero, filmes in catalogo.items():
        for filme, ano in filmes:
            if busca in filme.lower():
                encontrados.append((filme, ano, genero))
    if encontrados:
        print("Filme encontrado:")
        for filme, ano, genero in encontrados:
            print(f'{filme} {(30 - len(filme)) * " "} {ano} - Gênero: {genero}')
    else:
        print("Nenhum filme encontrado com esse título.")

def menu():
    while True:
        print("\n=== Catálogo de Filmes ===")
        print("1. Adicionar filme")
        print("2. Mostrar catálogo por gênero")
        print("3. Mostrar catálogo por filme")
        print("4. Remover filme")
        print("5. Buscar filme")
        print("6. Sair")
        
        escolha = input("Escolha uma opção (1-6): ")
        
        if escolha == '1':
            adicionar_filme(catalogo)
        elif escolha == '2':
            mostrar_catalogo(catalogo, "gênero")
        elif escolha == '3':
            mostrar_catalogo(catalogo, "filme")
        elif escolha == '4':
            remover_filme(catalogo)
        elif escolha == '5':
            buscar_filme(catalogo)
        elif escolha == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()