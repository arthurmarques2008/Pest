'''
Modifique a questão anterior para encontrar todos os números de Armstrong dado um intervalo.
'''

intervalo1 = int(input("Digite um número para o primeiro ponto do intervalo: "))

intervalo2 = int(input("Digite um número para o segundo ponto do intervalo: "))

contador = intervalo1

while intervalo2 >= contador:
    intervalo1_str = str(intervalo1)
    tamanho = len(intervalo1_str)
    soma = 0
    while contador > 0:
        dig = contador % 10
        soma += dig ** tamanho
        contador = contador // 10
    if soma == intervalo1:
        print(f"O número: {intervalo1} é um número de armstrong")
    else:
        print(f"O número: {intervalo1} não é um número de armstrong")
    intervalo1 += 1
    contador = intervalo1






