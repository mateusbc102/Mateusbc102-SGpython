import random

palavra_lista = ["lume"]

#,"trigo","bravo","folhas","mangas","planeta","riso","vento","canto","camada","tundra","oceano","nuvem","farol","rochas","selvas","caminho","estrela","flor","prado","campo","galhos","navegar","relógio","matriz"

palavra = random.choice(palavra_lista)
chances = len(palavra) + 2

print ("Vamos jogar? Está na hora de acertar a palavra no jogo da forca!")
print ("Teremos palavras aleatórias com 4, 5, 6 e 7 letras.")
print (f"Você terá {chances} chances para acertar a palavra selecionada.")

palpite = ""

if len(palavra) < 5:
    print (" _ _ _ _")
    letra_tentativa = input("Está pronto?! Tente acertar uma letra da palavra acima: ")
    while chances > 0 and palpite != palavra:
        if letra_tentativa in palavra:
            palpite += letra_tentativa
            print (palpite)            
            letra_tentativa = input("Letra correta! Tente acertar a próxima: ")
        else:
            chances -= 1
            letra_tentativa = input(f"Letra incorreta! Tente mais uma, você tem {chances} chances: ")
    if chances > 0 and palpite == palavra:
        print (f"Parabéns! Você acertou! A palavra era {palavra}, e ainda sobram {chances} chances!")
    else:
        print (f"infelizmente errou, a palavra era {palavra}.")


"""elif len(palavra) == 5:
    print ("_ _ _ _ _")
    letra_tentativa = input("Está pronto?! Tente acertar uma letra da palavra acima: ")
elif len (palavra) == 6:
    print ("_ _ _ _ _ _")
    letra_tentativa = input("Está pronto?! Tente acertar uma letra da palavra acima: ")
else:
    print ("_ _ _ _ _ _ _")
    letra_tentativa = input("Está pronto?! Tente acertar uma letra da palavra acima: ")
"""
