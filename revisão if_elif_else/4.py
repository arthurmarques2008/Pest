'''
Escreva um programa em Python para somar três números inteiros do usuário. 
No entanto, se dois valores forem iguais, a soma será zero.
'''


num1 = int(input("Digite um numero: "))
num2 = int(input("Digite o 2 numero: "))
num3 = int(input("Digite o 3 numero: "))
soma = num1 + num2 + num3
if num1 == num2 or num2 == num3 or num1 == num3:
    soma = 0
    print(f"Algum número é igual então o resultado da soma é igual a {soma}")
else:
    print(f"A soma é igual a {soma}")

