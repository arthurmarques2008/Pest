binario = int(input("Digite um número: "))
decimal = 0
potencia = 0

while binario > 0:
    ultimo_digito = binario%10
    decimal += ultimo_digito * (2 ** potencia)
    binario = binario//10
    potencia += 1

print(decimal)