'''
Gere um número aleatório entre 1 e 9 (incluindo 1 e 9). Peça ao usuário para adivinhar o número e diga se o número é muito baixo, 
muito alto ou se ele acertou. Caso ele digite “sair” o jogo deveacabar. OBS: import random e num = random.randint(1,9)
'''


import random

num = random.randint(1,9)
tentativa = 0

while tentativa != num:
    tentativa = int(input("Chute um número e tente acertar: "))
    if num > tentativa:
        print("Tente chutar um número maior")
    elif num < tentativa:
        print("Tente chutar um número menor")
    else:
        print("Você acertou")

