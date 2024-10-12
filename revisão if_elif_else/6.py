'''
Crie um programa para ler um número de 5 dígitos e verificar se existe algum dígito que se repete 2 ou mais vezes.
OBS: NÃO converta N para string. Trate-o como número!
'''

numero = int(input("Digite um número de 5 digitos: ")) #Para exemplificar pense nesse número como se ele fosse 12345

dig1 = numero % 10 # vai pegar sempre o ultimo digito, então vai pegar o 5 
dig2 = numero // 10 % 10 # vai pegar o 4
dig3 = numero // 100 % 10 # vai pegar o 3
dig4 = numero // 1000 % 10 # vai pegar o 2
dig5 = numero // 10000 % 10 # vai pegar o 1

if dig1 == dig2 or dig2 == dig3 or dig3 == dig4 or dig4 == dig5 or dig5 == dig1:
    print("Algum digito se repete")
else:
    print("Nenhum digito se repete")

