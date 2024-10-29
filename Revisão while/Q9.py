'''
Um inteiro positivo é chamado de número de Armstrong de ordem n se abc = a^n+b^n+c^n+... 
Crie um programa para verificar se um número n é um número de Armstrong.
Ex: 153 = 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3
'''
numero = input("Digite um número para verificar se ele é um número de armstrong: ")

tamanho_do_numero = len(numero)
numero = int(numero)

copia = numero
soma = 0
while numero > 0:
    dig = numero % 10
    soma += dig ** tamanho_do_numero
    numero = numero//10

if soma == copia:
    print(f"O número {soma}, é um número de armstrong!")
else:
    print(f"O número {copia}, não é um número de armstrong")

