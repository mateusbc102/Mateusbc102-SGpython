Menu = True
perseguição_nome = []
perseguição_distância = []
perseguição_tempo = []
perseguição_velocidade_média = []
quantidade_perseguições = 0
print("Bem vindo a Lista Terminal... ")
while Menu == True:
    pergunta_menu = input("""Escolha uma das opções abaixo para prosseguir na missão:
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
            escolha_nome = input(f"Qual o nome do {indice+1} fugitivo? ")
            perseguição_nome.append(escolha_nome)
            escolha_distância = float(input(f"Qual a distãncia em quilômetros da perseguição {indice+1}? "))
            perseguição_distância.append(escolha_distância)
            escolha_tempo = int(input(f"Qual o tempo em minutos da perseguição {indice+1}? "))
            perseguição_tempo.append(escolha_tempo)
            media = round(escolha_distância/(escolha_tempo/60), 2)
            perseguição_velocidade_média.append(media)
            print (f"A velocidade média é {media} km/h")
            if media >= 60:
                print ("Perseguição em alta velocidade, precisamos de um veículo!")
            elif media >= 20:
                print ("Perseguição urbana, precisamos de agilidade, mas cuidado!")
            else:
                print("Perseguição lenta, precisamos ser discretos, vamos a pé!")
        print("Perseguições registradas, retorne ao menu para a próxima etapa.")
    elif pergunta_menu.lower() == "listar perseguições" or pergunta_menu.lower() == "listar perseguicoes":
        if quantidade_perseguições <= 0:
            print("Sem perseguições registradas, retorne ao Menu principal")
        else:
            for nome in (perseguição_nome, perseguição_distância, perseguição_tempo):
                print(nome)
            print("Retorne ao Menu para prosseguir")
    elif pergunta_menu.lower() == "buscar fugitivo":
        if quantidade_perseguições <= 0:
            print("Sem fugitivos registrados, retorne ao Menu principal")
        else:
            fugitivo = input("Escreva o nome do fugitivo: ")
            for busca in perseguição_nome:
                if busca == fugitivo:
                    print(f"O fugitivo {fugitivo} está na lista de procurados, acione as autoridades imediatamente.")
                    break
            else:
                print(f"{fugitivo} não faz parte da lista de foragidos.")
    else:
        print("invalido")
