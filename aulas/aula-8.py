# Desempacotamento com *

'''
*x, y, z = (1, 2, 3, 4, 5)
print(x)  # [1, 2, 3]
print(y)  # 4
print(z)  # 5

a, *b, c = (1, 2, 3, 4, 5)
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

a, b, *c = (1, 2, 3, 4, 5)
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5]

'''

# combinando elementos de tuplas diferentes

'''
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla3 = tupla1 + (*tupla2,)

print(tupla3)  # (1, 2, 3, 4, 5, 6)
'''

# matrizes com tuplas


matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matriz) # ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(matriz[0])  # (1, 2, 3)
print(matriz[0][1])  # 2
print(matriz[1][2])  # 6

# iterando sobre uma matriz

for linha in matriz: # linha é uma tupla
    for elemento in linha: # elemento é um int
        print(elemento, end=" ") # imprime na mesma linha
    print()  # quebra de linha

# somando os elementos de uma matriz

soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento
print(soma)  # 45
