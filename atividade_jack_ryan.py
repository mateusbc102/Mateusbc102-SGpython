"""
Missão TACTUS: Operação Jack Ryan

Você faz parte da equipe de análise de inteligência da CIA e precisa ajudar o analista Jack Ryan a
rastrear uma transação financeira suspeita e verificar o status de segurança de um esconderijo inimigo.

Requisitos do Desafio:

Entrada de dados: O programa deve solicitar ao usuário o nome do agente em campo, o valor da
transferência financeira suspeita (como um número decimal) e o nível atual de
ameaça (um número inteiro de 1 a 5).

Validação e Limite: O programa deve usar uma estrutura de repetição para permitir que o usuário
insira o nome de até 3 alvos suspeitos. Se o usuário digitar a palavra "sair", o rastreamento
deve ser interrompido imediatamente (break).

Análise de Risco:

Se o valor da transferência for maior que 50000.0 e o nível de ameaça for maior ou igual a 4, o
status do esconderijo deve ser classificado como "Alerta Vermelho".

Caso contrário, se o nível de ameaça for maior ou igual a 2, o status deve ser "Alerta Amarelo".

Para qualquer outra situação, o status deve ser "Seguro"."""

valor_transferencia = 60000.00
nivel_ameaca = 6
quantidade_alvos = 3

while quantidade_alvos > 0:
    print ("Bem vindo a missão Tactus... Por favor insira os parâmetros da missão abaixo...")
    rastreamento = 3
    while rastreamento > 2:
        rastreamento = input('Está sendo rastreado no momento? Caso esteja digite "Sair", caso contrário "continuar" para proseguir: ' )
        if rastreamento == "Sair" or rastreamento == "sair" or rastreamento == "SAIR" or rastreamento == "sAIR":
            print ("Comunicação comprometida ... Status: Interrompido...")
            rastreamento = 1
            break
        elif rastreamento == "continuar" or rastreamento == "Continuar" or rastreamento == "CONTINUAR" or rastreamento == "cONTINUAR":
            print ("Comunicação Segura ... Status: Conectado")
            rastreamento = 2
        else:
            print ("Verificação inconsistente ... tente novamente ...")
            rastreamento = 3
    if rastreamento == 1:
        print ("Missão abortada...")
        break
    pergunta_agente = input("Qual o codinome do agente que efetuou a transação suspeita? ")
    pergunta_valor_transferencia = input("Qual o valor em reais da transferência analisada? ")
    while pergunta_valor_transferencia == str:
        print ("Valor inconsistente, tente novamente ...")
        pergunta_valor_transferencia = input("Qual o valor em reais da transferência analisada? ")
        
    pergunta_nivel_amaeaca = int(input("Qual o nível de ameaça classificado pelo chefe da estação entre 1 e 4? "))
    #if valor_transferencia
