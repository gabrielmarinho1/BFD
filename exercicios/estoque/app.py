# cadastro
# editar
# listar
# buscar
# menu

import csv

def get_last_csv_line(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        lines = list(reader)
        if lines:
            return lines[-1]
        return None
def cadastrar():
    with open('estoque.csv', mode='a', newline='\n') as file:
        writer = csv.writer(file)
        id = int(get_last_csv_line('estoque.csv')[0]) + 1
        nome = input("Digite o nome do produto: ")
        quantidade = input("Digite a quantidade no estoque: ")
        preco = input("Digite o preço do produto: ")
        categoria = input("Digite a categoria do produto: ")
        produto = [id, nome, quantidade, preco, categoria]
        writer.writerow(produto)
    print("Cadastro realizado com sucesso!")
def listar():
    with open('estoque.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        print(f"{'ID':<5} {'Nome':<20} {'Quantidade':<10} {'Preço':<10} {'Categoria':<15}")
        print("-" * 60)
        for row in reader:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<10} {row[3]:<10} {row[4]:<15}")
def buscar():
    termo = input("Digite o nome ou categoria do produto que deseja buscar: ").lower()
    with open('estoque.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        resultados = [row for row in reader if termo in row[1].lower() or termo in row[4].lower()]
        if resultados:
            print(f"{'ID':<5} {'Nome':<20} {'Quantidade':<10} {'Preço':<10} {'Categoria':<15}")
            print("-" * 60)
            for row in resultados:
                print(f"{row[0]:<5} {row[1]:<20} {row[2]:<10} {row[3]:<10} {row[4]:<15}")
        else:
            print("Nenhum produto encontrado.")
def editar():
    buscar()
    id = input("Digite o ID do produto que deseja editar: ")
    with open('estoque.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        linhas = list(reader)
    for i, row in enumerate(linhas):
        if row[0] == id:
            print("Deixe em branco para manter o valor atual.")
            quantidade = input(f"Quantidade ({row[2]}): ") or row[2]
            preco = input(f"Preço ({row[3]}): ") or row[3]
            linhas[i] = [id, row[1], quantidade, preco, row[4]]

            with open('estoque.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(linhas)
            print("Produto atualizado com sucesso!")
            break
    
    listar()
def menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Buscar Produto")
        print("4. Editar Produto")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            cadastrar()
        elif escolha == '2':
            listar()
        elif escolha == '3':
            buscar()
        elif escolha == '4':
            editar()
        elif escolha == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()