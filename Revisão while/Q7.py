'''
Escreva um programa para escrever todos os números de 1 a 100. Onde tiver um múltiplo de 3, troque por “Fizz”. 
Onde tiver um múltiplo de 5, troque por “Buzz”. Para os múltiplos de 3 e 5 ao mesmo tempo, troque por “FizzBuzz”.
'''


contador = 0

while contador < 100:
    contador += 1
    if contador % 3 == 0 and contador % 5 == 0:
        print("FizzBuzz")
    elif contador % 3 == 0:
        print("Fizz")
    elif contador % 5 == 0:
        print("Buzz")
    else:
        print(contador)
    