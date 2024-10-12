'''
Escreva um código em Python que utilize a estrutura de controle if-elif-else para verificar se um número inteiro 
dado é par ou ímpar. Se o número for par, armazene-o em uma variável chamada 'pares' e se for ímpar, 
armazene-o em uma variável chamada 'impares'. Utilize uma única linha de código dentro do bloco 'if' e outra dentro 
do bloco else.
OBS: considere zero como neutro (nem par, nem ímpar).
'''
numero = int(input("Digite um número: "))

if numero % 2 == 0: # Todos os números pares quando são divididos por 2 o resto deles vai ser 0
    par = numero
else:
    impar = numero