palavra = "python"
letras_usuario = []
tentativa_lista = []
chances = 4
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você possui {chances} chances.")
    tentativa = input(f"Escolha uma letra para adivinhar:\nVocê já tentou essas letras {tentativa_lista}. ")
    tentativa_lista.append(tentativa)
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -=1
    
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, você ganhou. A palavra era: {palavra}.")
else:
    print(f"Você perdeu. A palavra era {palavra}.")
