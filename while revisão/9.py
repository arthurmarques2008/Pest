num = int(input("Digite um número: "))
copia = num
num_str = str(num)
soma = 0
while num > 0:
    ultimo_digito = num%10
    soma += ultimo_digito**len(num_str)
    num = num//10

if soma == copia:
    print("O número é um armstrong")
else:
    print("Não é um número de armstrong")


