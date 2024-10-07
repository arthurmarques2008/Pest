soma = 0
while True:
    numero = int(input("Digite um número: "))
    soma += numero
    if numero == 0:
        print(soma)
        break