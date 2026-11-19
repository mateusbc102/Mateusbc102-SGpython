import random
progresso = []
pedras = ["Agarrão", "Romba", "Pinça", "Buraco", "Chaminé"]
movimentos = ["Esticar braços", "Descanso", "Movimento fluido", "Apressar passagem"]

while len(progresso) < 6:
    print(f"Seu progresso é: {progresso}.")
    proxima_pedra = pedras[random.randint(0,4)]
    escolha = input(f"\nSua próxima pedra é: {proxima_pedra}. Qual movimento você deseja fazer?\n{movimentos}\nEscolha: ")
    if proxima_pedra == "Agarrão":
        if escolha.lower() == "esticar braços" or escolha.lower() == "esticar bracos":
            progresso.append(proxima_pedra)
            print(f"\nParabéns! Você subiu a pedra {proxima_pedra} e avançou para o {len(progresso)+1}° nível.\n")
        elif escolha.lower() == "apressar passagem":
            progresso.clear()
            print("Você caiu no chão e perdeu todo o progresso.")
        elif escolha in movimentos:
            print("Seu movimento o sustenta, mas não progride. Tente uma pedra ao lado.")
        else:
            print("Inválido")
    elif proxima_pedra == "Romba":
        if escolha.lower() == "movimento fluido" or escolha.lower() == "movimento fluído":
            progresso.append(proxima_pedra)
            print(f"\nParabéns! Você subiu a pedra {proxima_pedra} e avançou para o {len(progresso)+1}° nível.\n")
        elif escolha.lower() == "esticar braços" or escolha.lower() == "esticar bracos":
            progresso.clear()
            print("Você caiu no chão e perdeu todo o progresso.")
        elif escolha in movimentos:
            print("Seu movimento o sustenta, mas não progride. Tente uma pedra ao lado.")
        else:
            print("Inválido")
    elif proxima_pedra == "Pinça":
        if escolha.lower() == "apressar a passagem":
            progresso.append(proxima_pedra)
            print(f"\nParabéns! Você subiu a pedra {proxima_pedra} e avançou para o {len(progresso)+1}° nível.\n")
        elif escolha.lower() == "movimento fluído" or escolha.lower() == "movimento fluido":
            progresso.clear()
            print("Você caiu no chão e perdeu todo o progresso.")
        elif escolha in movimentos:
            print("Seu movimento o sustenta, mas não progride. Tente uma pedra ao lado.")
        else:
            print("Inválido")
    elif proxima_pedra == "Buraco":
        if escolha.lower() == "esticar braços" or escolha.lower() == "esticar bracos":
            progresso.append(proxima_pedra)
            print(f"\nParabéns! Você subiu a pedra {proxima_pedra} e avançou para o {len(progresso)+1}° nível.\n")
        elif escolha.lower() == "movimento fluído" or escolha.lower() == "movimento fluido":
            progresso.clear()
            print("Você caiu no chão e perdeu todo o progresso.")
        elif escolha in movimentos:
            print("Seu movimento o sustenta, mas não progride. Tente uma pedra ao lado.")
        else:
            print("Inválido")
    else:
        if escolha.lower() == "apressar passagem":
            progresso.append(proxima_pedra)
            print(f"\nParabéns! Você subiu a pedra {proxima_pedra} e avançou para o {len(progresso)+1}° nível.\n")
        elif escolha.lower() == "esticar braços" or escolha.lower() == "esticar bracos":
            progresso.clear()
            print("Você caiu no chão e perdeu todo o progresso.")
        elif escolha in movimentos:
            print("Seu movimento o sustenta, mas não progride. Tente uma pedra ao lado.")
        else:
            print("Inválido")
print(f"Parabéns! Você chegou ao topo e venceu a montanha. Seu progresso é: {progresso}.")
