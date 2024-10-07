num = int(input("Digite um número: "))
invertido = 0

while num>0:
    ultimo_digito = num%10
    invertido = invertido * 10 + ultimo_digito
    num = num//10

print(invertido)