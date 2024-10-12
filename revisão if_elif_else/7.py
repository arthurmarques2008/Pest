numero = int(input("Digite um número de três digitos: "))

dig1 = numero % 10
dig2 = numero // 10 % 10
dig3 = numero // 100 % 10

if dig1 == dig3:
    print(f"O número: {numero} é palíndromo")
else:
    print(f"O número: {numero} não é palíndromo")
    
'''
Para verificar se um número é palíndromo você deve olhar para as extremidades se elas forem iguais então ele será
palíndromo.
para exemplificar pense no número 101: você pode ver que o número das extremidades é igual '1' então ele é palíndromo
'''