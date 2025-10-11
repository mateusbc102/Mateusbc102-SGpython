trabalhoEstressante = input ('Seu trabalho é estressante? (Responda com "s" ou "n")')
tempoDeTrabalho = input ('Quantas horas de trabalho diario? ')
FazAtividadeFisica = input ('Faz atividade fisica semanalmente?(Responda com "s" ou "n")')
alimentacaoRuim = input ('Sua alimentação é inadequada? (Responda com "s" ou "n")')
if trabalhoEstressante == 's':
  if int(tempoDeTrabalho) > 6:
    if FazAtividadeFisica == 'n':
      if alimentacaoRuim == 's':
        print ('cuidado!')
      else:
        print ('Pelo menos come bem!')
    else:
      if alimentacaoRuim == 's':
        print ('no meio do caminho!')
      else:
        print ('Na hora de pedir demissão!')
  else:
    if FazAtividadeFisica == 'n':
      if alimentacaoRuim == 's':
        print ('atenção!')
else:
  if int(tempoDeTrabalho) > 6:
    if FazAtividadeFisica == 'n':
      if alimentacaoRuim == 's':
        print ('atenção!')
