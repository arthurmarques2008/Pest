x1 = float(input("Digite O número de X1: "))
x2 = float(input("Digite o número de x2: "))
y1 = float(input("Digite o número de y1: "))
y2 = float(input("Digite o número de y2: "))

delta_x = (x2 - x1) ** 2
delta_y = (y2 - y1) ** 2

distancia = (delta_x + delta_y) ** 0.5

print(distancia)