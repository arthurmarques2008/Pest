'''
Crie um programa para converter de binário para decimal usando while.
'''

numero = int(input("Digite um número binário: "))
decimal = 0
expoente = 0
while numero > 0:
    dig = numero % 10
    decimal += (2 ** expoente) * dig
    numero = numero // 10
    expoente += 1

print(decimal)

