capa_do_livro = 24.95
contador = 0
preço_total = 0
while contador <= 60:
    preço_total += capa_do_livro
    contador += 1
preço_com_desconto = preço_total*(40/100)
entrega = (59*0.75)+3

preço_total_do_produto = preço_com_desconto+entrega

print(f"O preço com desconto é {preço_total_do_produto}")
print(f"O preço sem o desconto é {preço_total+entrega}")


    