hora_atual = int(input("Digite a hora atual do relogio: "))
hora_adicional = int(input("Digite a hora a ser adicionada no relogio: "))

alarme = (hora_atual+hora_adicional)%24

print(f"{alarme} horas")