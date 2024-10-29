'''
Crie um código em Python que use o comando "while" para ler números inteiros inseridos pelo usuário até que o 
número inserido seja zero e imprima a soma de todos os números inseridos.
'''

numero = 5
soma = 0
while numero != 0:
    numero = int(input("Digite um número ou 0 para parar: "))
    soma += numero

print(f"O resultado da soma: {soma}")
