'''
Crie um código em Python que solicite ao usuário um número e, usando o comando "while", imprima todos os divisores 
desse número até que o usuário digite "0" para encerrar o programa.
'''
numero = int(input("Digite um número: "))
contador = 0

while contador != numero:
    verificar = input("Digite 0 para parar o código ou digite qualquer outra coisa para continuar: ")
    if verificar == '0':
        break
    contador += 1
    if numero % contador == 0:
        print(f"{contador} é divisor de {numero}")
