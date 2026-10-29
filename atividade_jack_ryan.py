print ("Bem vindo a missão Tactus... Por favor insira os parâmetros da missão abaixo...")
rastreamento = 3
seguranca = True
while seguranca == True:
    while rastreamento > 2:
        rastreamento = input('Está sendo rastreado no momento? Caso esteja digite "Sair", caso contrário "continuar" para proseguir: ' )
        if rastreamento.lower() == "sair":
            print ("Comunicação comprometida ... Status: Interrompido...")
            rastreamento = 1
            seguranca = False
        elif rastreamento.lower() == "continuar":
            print ("Comunicação Segura ... Status: Conectado")
            rastreamento = 2
        else:
            print ("Verificação inconsistente ... tente novamente ...")
            rastreamento = 3
    if seguranca == False:
        break
    quantidade_amarelo = 0
    quantidade_vermelho = 0
    while quantidade_amarelo < 3 and quantidade_vermelho < 2:
        pergunta_agente = input("Qual o codinome do agente que efetuou a transação suspeita? ")
        if pergunta_agente == "sair":
            print ("Operação encerrada...")
            break
        pergunta_valor_transferencia = input("Qual o valor em reais da transferência analisada? ")
        lista_de_numeros = [".","0","1","2","3","4","5","6","7","8","9"]
        escreveu_errado = True
        quantos_pontos = 0
        while escreveu_errado == True:
            escreveu_errado = False        
            for digito in pergunta_valor_transferencia:
                if digito not in lista_de_numeros:
                    escreveu_errado = True
                    print (f"Esse dígito {digito} não é um número")
                if digito == ".":
                    quantos_pontos += 1
            if escreveu_errado == True or quantos_pontos > 1:
                pergunta_valor_transferencia = input("Tente novamente. Qual o valor em reais da transferência analisada? ")
            else:
                pergunta_valor_transferencia = float(pergunta_valor_transferencia)
        pergunta_nivel_amaeaca = int(input("Qual o nível de ameaça classificado pelo chefe da estação entre 1 e 5? "))
        while pergunta_nivel_amaeaca > 5 or pergunta_nivel_amaeaca < 1:
            print ("Nível insirido inválido, tente novamente.")
            pergunta_nivel_amaeaca = int(input("Qual o nível de ameaça classificado pelo chefe da estação entre 1 e 5? "))       
        if pergunta_nivel_amaeaca >= 4 and pergunta_valor_transferencia >= 50000.00:
            print("Operador suspeito identificado. Alerta Vermelho")
            quantidade_vermelho += 1
        elif pergunta_nivel_amaeaca >= 2 and pergunta_valor_transferencia >= 10000.00:
            print ("Operador em análise. Alerta Amarelo")
            quantidade_amarelo += 1
        else:
            print ("Transação Segura, suspeito descartado.")
    print (f"Operação comprometida, tivemos {quantidade_vermelho} Alerta Vermelho e {quantidade_amarelo} Alerta Amarelo. Abandonar estação.")
    break
