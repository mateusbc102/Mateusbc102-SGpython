import random

print ("Vamos Jogar?")

chances = int(input("Escolha quantas chances deseja ter para acertar o número secreto: "))
while chances <= 0:
    print ("Numero escolhido menor que o mínimo.")
    chances = int(input("Escolha quantas chances deseja ter para acertar o número secreto: "))

maximo = int(input("Escolha o intervalo máximo em que o número secreto deve estar: "))
while maximo <= 1:
    print ("Numero escolhido menor que o mínimo para o intervalo.")
    maximo = int(input("Escolha o intervalo máximo em que o número secreto deve estar: "))

numero_secreto = random.randint(1,maximo)
numero_escolhido = 0

while numero_secreto != numero_escolhido and chances > 0:

    numero_escolhido = int(input(f"Escolha um numero para adivinhar (Escolha de 1 a {maximo}): "))
    while numero_escolhido < 1 or numero_escolhido > maximo:
        print ("Numero escolhido fora do intervalo.")
        numero_escolhido = int(input(f"Escolha um numero para adivinhar (Escolha de 1 a {maximo}): "))
        
    chances -= 1

    if numero_secreto == numero_escolhido and chances == 0:
        print (f"Acertou! O numero era {numero_secreto}. E não sobraram chances.")
    elif numero_secreto == numero_escolhido:
         print (f"Acertou! O numero era {numero_secreto}. E ainda sobraram {chances} chances.")
    elif numero_secreto < numero_escolhido:
        print (f"Errou, o numero secreto é menor do que esse. Voce possui {chances} chances.")
    else:
        print(f"Errou, o numero secreto é maior do que esse. Voce possui {chances} chances.")
    
if chances == 0 and numero_secreto != numero_escolhido:
    print (f"Voce perdeu todas as chances, o número era {numero_secreto}.")
