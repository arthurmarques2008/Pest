import random

num = random.randint(1,9)

while True:
    tentativa = input("Tente acertar um número entre 1 e 9 ou digite sair para acabar: ")
    if tentativa == 'sair':
        print("O jogo acabou")
        break
    else:
        tentativa = int(tentativa)
        if tentativa == num:
            print("Você ganhou!")
        elif tentativa >= 5:
            print("Muito alto")
        elif tentativa <= 4:
            print("Muito baixo")    