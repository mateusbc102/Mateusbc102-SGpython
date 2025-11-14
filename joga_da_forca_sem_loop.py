palavra = "animal"
print ("Esse é o jogo da forca, tente acertar a palavra antes de perder todas as chances!")
print ("_ _ _ _ _ _")
palpite = input ("Coloque a seguir qual letra voce acha que é: ")
if palpite == palavra[0]:
    print("a _ _ _ a _")
    palpite = input ("Coloque a seguir qual letra voce acha que é: ")
    if palpite == palavra[1]:
        print ("a n _ _ a _")
        palpite = input ("Coloque a seguir qual letra voce acha que é: ")
        if palpite == palavra[2]:
            print ("a n i _ a _")
            palpite = input ("Coloque a seguir qual letra voce acha que é: ")
            if palpite == palavra[3]:
                print("a n i m a _")
                palpite = input ("Coloque a seguir qual letra voce acha que é: ")
                if palpite == palavra[5]:
                    print("a n i m a l")
                    print ("Parabéns! Você acertou a palavra!")
                else:
                    print("Perdeu")
            elif palpite == palavra[5]:
                print("a n i _ a l")
            else:
                print("Perdeu")
        elif palpite == palavra[3]:
            print("a n _ m a _")

        elif palpite == palavra[5]:
            print("a n _ _ a l")
        else:
            print("Perdeu")
    elif palpite == palavra[2]:
        print ("a _ i _ a _")
    elif palpite == palavra[3]:
        print("a _ _ m a _")
    elif palpite == palavra[5]:
        print("a _ _ _ a l")
    else:
        print("Perdeu")
elif palpite == palavra[1]:
    print ("_ n _ _ _ _")
elif palpite == palavra[2]:
    print ("_ _ i _ _ _")
elif palpite == palavra[3]:
    print("_ _ _ m _ _")
elif palpite == palavra[5]:
    print("_ _ _ _ _ l")
else:
    print("Perdeu")

"""
palpite == palavra[1]:
    print ("_ n _ _ _ _")
elif palpite == palavra[2]:
    print ("_ _ i _ _ _")
elif palpite == palavra[3]:
    print("_ _ _ m _ _")
elif palpite == palavra[5]:
    print("_ _ _ _ _ l")
else:
    print("Perdeu")
"""
