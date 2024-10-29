'''
Crie um código em Python que peça ao usuário para digitar um número inteiro positivo, e então utilize o comando 
"while" para imprimir cada número até chegar ao número digitado pelo usuário.
'''

contador = 1
numero = int(input("Digite um número: "))

while contador <= numero:
    print(contador)
    contador += 1