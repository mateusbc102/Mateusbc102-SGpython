idade = float(input('Qual a sua idade? '))
experiencia = input('Tem experiencia? (s/n) ')
antecedentes_criminais = input('possui antecedentes criminais? (s/n) ')
ensino_superior = input('Possui ensino superior? (s/n) ')
indicaçao = input('Foi indicado por alguem? (s/n) ')
if antecedentes_criminais == 's':
    print('Infelizmente nao temos vagas disponiveis.')
elif idade >= 18 and (experiencia == 's' or (ensino_superior == 's' or indicaçao =='s')):
    print ('Voce foi chamado para entrevista.')
else:
    print ('Infelizmente outro candidato foi escolhido.')
