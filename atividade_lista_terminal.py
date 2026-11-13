Menu = True
perseguição_nome = []
perseguição_distância = []
perseguição_tempo = []
perseguição_velocidade_média = []
print("Bem vindo a Lista Terminal... ")
while Menu == True:
    pergunta_menu = input("""
    Escolha uma das opções abaixo para prosseguir na missão:
    Registrar perseguição 
    Listar perseguições 
    Buscar fugitivo 
    Remover fugitivo 
    Estatísticas 
    Sair 
    Escreva: """)
    if pergunta_menu.lower() == "sair":
        print("Missão abortada")
        Menu = False
    elif pergunta_menu.lower() == "registrar perseguição" or pergunta_menu.lower() == "registrar perseguicao":
        quantidade_perseguições = int(input("Quantas perseguições deseja registrar? "))
        for indice in range(quantidade_perseguições):
            escolha_nome = input(f"\nQual o nome do {indice+1} fugitivo? ")
            perseguição_nome.append(escolha_nome)
            escolha_distância = float(input(f"Qual a distãncia em quilômetros da perseguição {indice+1}? "))
            perseguição_distância.append(escolha_distância)
            escolha_tempo = int(input(f"Qual o tempo em minutos da perseguição {indice+1}? "))
            perseguição_tempo.append(escolha_tempo)
            media = round(escolha_distância/(escolha_tempo/60), 2)
            perseguição_velocidade_média.append(media)
            print (f"\nA velocidade média é {media} km/h")
            if media >= 60:
                print ("\nPerseguição em alta velocidade, precisamos de um veículo!")
            elif media >= 20:
                print ("\nPerseguição urbana, precisamos de agilidade, mas cuidado!")
            else:
                print("\nPerseguição lenta, precisamos ser discretos, vamos a pé!")
        print("\nPerseguições registradas, retorne ao menu para a próxima etapa.")
    elif pergunta_menu.lower() == "listar perseguições" or pergunta_menu.lower() == "listar perseguicoes":
        if len(perseguição_nome) == 0:
            print("Sem perseguições registradas, retorne ao Menu principal")
        else:
            for indice in range(len(perseguição_nome)):
                print(f"Nome: {perseguição_nome[indice]}, Velocidade: {perseguição_velocidade_média[indice]} Km/h, Tempo: {perseguição_tempo[indice]} min, Distância: {perseguição_distância[indice]} Km")               
            print("Retorne ao Menu para prosseguir")
    elif pergunta_menu.lower() == "buscar fugitivo":
        if len(perseguição_nome) == 0:
            print("Sem fugitivos registrados, retorne ao Menu principal")
        else:
            fugitivo = input("Escreva o nome do fugitivo: ")
            encontrou = False
            for indice in range(len(perseguição_nome)):
                if perseguição_nome[indice] == fugitivo:
                    print(f"O fugitivo {fugitivo} está na lista de procurados, acione as autoridades imediatamente.")
                    print(f"Nome: {perseguição_nome[indice]}, Velocidade: {perseguição_velocidade_média[indice]} Km/h, Tempo: {perseguição_tempo[indice]} min, Distância: {perseguição_distância[indice]} Km")
                    encontrou = True
            if encontrou == False:
                print(f"{fugitivo} não faz parte da lista de foragidos.")
    elif pergunta_menu.lower() == "remover fugitivo":
        if len(perseguição_nome) == 0:
            print("Sem fugitivos registrados, retorne ao Menu principal")
        else:
            fugitivo = input("Escreva o nome do fugitivo: ")
            encontrou = False
            for indice in range(len(perseguição_nome)):
                if perseguição_nome[indice] == fugitivo:
                    perseguição_nome[indice] = "removido"
                    perseguição_distância[indice] = 0
                    perseguição_tempo[indice] = 0
                    perseguição_velocidade_média[indice] = 0
                    print(f"O fugitivo {fugitivo} foi removido do registro.")
                    encontrou = True
            if encontrou == False:
                print(f"{fugitivo} não faz parte da lista de foragidos.")
    elif pergunta_menu.lower() == "estatisticas" or pergunta_menu.lower() == "estatísticas":
        if len(perseguição_nome) == 0:
            print("Sem fugitivos registrados, retorne ao Menu principal")
        else:
            distância_total = 0
            nome_perseguição_longa = ""
            perseguição_longa = 0
            nome_fugitivo_rápido = ""
            fugitivo_rápido = 0
            quantidade_alta_velocidade = 0
            for indice in range(len(perseguição_nome)):
                distância_total += perseguição_distância[indice]
                if perseguição_longa < perseguição_distância[indice]:
                    perseguição_longa = perseguição_distância[indice]
                    nome_perseguição_longa = perseguição_nome[indice]
                if fugitivo_rápido < perseguição_velocidade_média[indice]:
                    fugitivo_rápido = perseguição_velocidade_média[indice]
                    nome_fugitivo_rápido = perseguição_nome[indice]
            print(f"Distância total: {distância_total} km, Distância média: {distância_total/len(perseguição_nome)} km\nNome do Fugitivo com Perseguição mais longa: {nome_perseguição_longa}, Nome do fugitivo com Perseguição mais rápida: {nome_fugitivo_rápido}.")
    else:
        print("\n    Inválido")
