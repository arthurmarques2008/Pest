'''
Leia um número N e escreva esse número ao contrário usando while.
OBS: NÃO converta N para string. Trate-o como número!
'''


numero = int(input("Digite um número: "))
numero_invertido = 0
while numero != 0:
    dig = numero % 10
    numero_invertido = dig + (numero_invertido*10)
    numero = numero//10

print(numero_invertido)
