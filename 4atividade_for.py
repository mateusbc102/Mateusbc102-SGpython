perguntas_lista = ["Quantos estados o Brasil possui?", "Quantas regioes o Brasil tem?","Qual a capital do Ceará"]
respostas_lista = ["26","5","fortaleza"]
acertos = 0

for indice in range (len(perguntas_lista)) :
    print(perguntas_lista[indice])
    resposta = input("Escreva sua resposta: ")
    if indice<2:
        if resposta == respostas_lista[indice]:
            print("Resposta correta")
            acertos += 1
        elif resposta == "":
            print ("Nao escreveu")
        else:
            print ("resposta errada.")
    else:
        if resposta.lower() == respostas_lista[indice]:
            print("Resposta correta")
            acertos += 1
        elif resposta == "":
            print ("Nao escreveu")
        else:
            print ("resposta errada.")
if acertos == 3:
    print("Parabens, acertou todas!")
elif acertos == 2:
    print ("Parabens, acetou 2!")
elif acertos == 1:
    print ("Parabens, acetou 1!")
else:
    print ("Infelizmente errou tudo")
