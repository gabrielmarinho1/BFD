cardapio = ("Hambúrguer","Cheeseburguer","Cachorro-quente","Batata frita","Refrigerante","Suco","Salada")

precos = [12.0, 13.5, 10.0, 8.0, 6.0, 7.5, 9.0]

conta = 0

print('\n===cardápio do dia===\n')

for index, lanche in enumerate(cardapio, start=1):
    spaces = "-" * (25 - len(lanche))
    print(f'{index} - {lanche} {spaces} R$ {precos[index-1]:.2f}')

while True:
    escolha = int(input('\nescolha um lanche (0 para finalizar): '))

    if escolha == 0:
        break
    else:
        conta += precos[escolha-1]
        print(f'\nvocê escolheu {cardapio[escolha-1]} por R$ {precos[escolha-1]:.2f}')

print(f'\nconta final: R$ {conta:.2f}\n')