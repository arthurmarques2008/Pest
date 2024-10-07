contador = 0
numero = int(input("Digite um número: "))
while contador < numero:
    contador += 1
    controlador = input("Digite 0 para parar o código ou digite 1 para continuar: ")
    if numero%contador == 0:
        print(contador)
    