vida_heroi = 10
vida_monstro = 10
espada = 3
raio = 6
quantidade_raio = 1
ataque_monstro = 5
cura = 6
quantidade_cura = 1

print (f"Voce e um paladino que precisa enfrentar um monstro antes que ele destrua a cidade. Voce possui {vida_heroi} de vida e ele tambem. O ataque dele diminui {ataque_monstro} de vida, e voce possui os seguintes ataques: Raio -{raio} e espada -{espada}. Alem disso, pode recuperar {cura} de vida. Sao apenas 4 rodadas antes dele destruir a cidade, nos ajude!")

for rodada in range (5):
    acao = input("Qual a sua acao? (Espada, Raio ou Cura?) ").lower()
    if acao  == "espada":
        vida_monstro -= 3
        if vida_monstro > 0:
            vida_heroi -= 5
            print(f"Voce atacou e tirou 3 de dano, mas ele se defendeu e tirou 5. Voce tem {vida_heroi} de vida e ele possui {vida_monstro} de vida.")
        else:
            break
    elif acao == "raio" and quantidade_raio == 1:
        quantidade_raio -= 1
        vida_monstro -= 6
        if vida_monstro > 0:
            vida_heroi -= 5
            print(f"Voce atacou e tirou 6 de dano, mas ele se defendeu e tirou 5. Voce tem {vida_heroi} de vida e ele possui {vida_monstro} de vida.")
        else: 
            break
    elif acao == "cura" and quantidade_cura == 1:
        quantidade_cura -= 1
        vida_heroi += 6
        vida_heroi -= 5
        print(f"Voce se curou e ganhou 6 de vida, mas ele te atacou e tirou 5. Voce tem {vida_heroi} de vida e ele possui {vida_monstro} de vida.")
    else:
        vida_heroi -= 5
        print(f"Acao invalida. Levou dano atoa. Voce tem {vida_heroi} de vida e ele possui {vida_monstro} de vida.")
    
    if vida_heroi <= 0:
        break
        
    
if vida_heroi > 0:
     print("Parabens! Voce derrotou o monstro e salvou nossa cidade. Cantaremos musicas em sua homenagem, construiremos estatuas e escreveremos historia em seu nome!")
else:
     print ("Voce falhou, mas seus esforcos serao lembrados.")
