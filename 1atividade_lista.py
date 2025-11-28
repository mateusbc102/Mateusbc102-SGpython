Lista_oficial = ["mateus","gabriel","juninho","sarah","guilherme","clarice","garibalda"]

indice_usuario = int(input("Escolha um numero da chamada: "))
if indice_usuario >= 0 and indice_usuario <  len(Lista_oficial):
    print (Lista_oficial[indice_usuario])
elif indice_usuario < 0:
    print ("Valor abaixo do permitido.")
elif indice_usuario > len(Lista_oficial)-1:
    print ("Valor maior do que permitido.")
