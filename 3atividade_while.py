capricho = 10
ingredientes = 10
nivel = 8
while nivel >= 8 and nivel <= 12 and nivel != 10:
    pergunta_ingredientes = float(input( "Quantos ingredientes você deseja usar? "))
    pergunta_capricho = float(input("Quanto de capricho você deseja usar nesse prato? "))
    if pergunta_ingredientes > ingredientes:
        pergunta_ingredientes = ingredientes
        ingredientes = 0
    elif pergunta_ingredientes < 0:
        pergunta_ingredientes = 0
    else:
        ingredientes -= pergunta_ingredientes
    if pergunta_capricho > capricho:
        pergunta_capricho = capricho
        capricho = 0
    elif pergunta_capricho < 0:
        pergunta_capricho = 0
    else:
        capricho -= pergunta_capricho
    nivel = 1.5 * pergunta_capricho + pergunta_ingredientes - 3
    if nivel == 10:
        print(f"Parabéns! O crítico ficou impressionado, seu prato alcançou o nível {nivel} e ganhou uma estrela Michelin")
    elif nivel >= 8 and nivel <= 12:
        print(f"O crítico teve uma opinião neutra sobre o prato. Ele alcançou o nível {nivel}, pode apresentar outro prato.")
        print(f"Restam {ingredientes} ingredientes e {capricho} pontos de capricho.")
    elif nivel > 12:
        print(f"Você exagerou, seu prato alcançou o nível {nivel}. O crítico ficou horrorizado e foi embora.")
    else:
        print(f"Você é a vergonha da profissão, seu prato alcançou o nível {nivel}. O crítico ficou horrorizado e foi embora.")
