import random
lista_pontos = [10,5,15,30,50]
lista_vilão = ["faca", "retrato da mãe", "tocha", "espada", "grimório"]
mochila = []
indice = 0
vida = 60
print("Você derrotou Valdemort, aproveite os despojos.")
while indice < len(lista_vilão) and vida > 0:
    print(f"Você possui {vida} pontos de vida.")
    escolha = input(f"Você deseja pegar esse item {lista_vilão[indice]} do vilão? (Escolha sim ou não): ")
    if escolha.lower() == "sim":
        amaldicoado = random.randint(0,1)
        if amaldicoado == 0:
            vida -= lista_pontos[indice]
            mochila.append(lista_vilão[indice] + " amaldiçoada")
            print(f"Você coletou o item {lista_vilão[indice]} amaldiçoada, perdeu {lista_pontos[indice]} pontos.")
        else:
            vida += lista_pontos[indice]
            mochila.append(lista_vilão[indice] + " abençoada")
            print(f"Você coletou o item {lista_vilão[indice]} abençoada, ganhou {lista_pontos[indice]} pontos.")
    else:
        print (f"Você não coletou o item {lista_vilão[indice]}")
    indice += 1
if vida > 0:
    print(f"Você coletou os itens {mochila} e possui {vida} pontos de vida. ")
else:
    print(f"Você morreu com {vida} pontos de vida e com os itens {mochila}.")
