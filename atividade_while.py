numero_escolhido = 0
numero_secreto = 7
while numero_secreto != numero_escolhido:
    numero_escolhido = int(input("Escolha um numero para adivinhar (Escolha de 1 a 10): "))
    if numero_secreto == numero_escolhido:
        print (f"Acertou! O numero era {numero_secreto}")
    elif numero_secreto < numero_escolhido:
        print ("Errou, o numero secreto é menor do que esse.")
    else:
        print("Errou, o numero secreto é maior do que esse.")
