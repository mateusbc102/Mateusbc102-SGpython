lista_vilão = ["faca", "retrato da mãe", "tocha", "espada", "grimório"]
mochila = []
print("Você derrotou Valdemort, aproveite os despojos.")
for item in lista_vilão:
    escolha = input(f"Você deseja pegar esse item {item} do vilão? (Escolha sim ou não): ")
    if escolha.lower() == "sim":
        mochila.append(item)
        print(f"Você coletou o item {item}. ")
    else:
        print (f"Você não coletou o item {item}")
print(f"Você coletou os itens {mochila}. ")
