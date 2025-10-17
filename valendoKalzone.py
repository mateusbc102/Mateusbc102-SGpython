trabalhoEstressante = input ('Seu trabalho é estressante? (Responda com "s" ou "n")')
if trabalhoEstressante == 's' or  trabalhoEstressante == 'n':
  tempoDeTrabalho = float( input ('Quantas horas de trabalho diario? '))
  fazAtividadeFisica = input ('Faz atividade fisica semanalmente?(Responda com "s" ou "n")')
  if fazAtividadeFisica == 's' or  fazAtividadeFisica == 'n':
    alimentacaoRuim = input ('Sua alimentação é inadequada? (Responda com "s" ou "n")')
    if alimentacaoRuim == 's' or  alimentacaoRuim == 'n':
      if trabalhoEstressante == 's':
        if (tempoDeTrabalho) > 6:
          if fazAtividadeFisica == 'n':
            if alimentacaoRuim == 's':
              print ('cuidado!')
            else:
              print ('Pelo menos come bem!')
          else:
            if alimentacaoRuim == 's':
              print ('Apenas 1 de 4!')
            else:
              print ('Na hora de pedir demissão!')
        else:
          if fazAtividadeFisica == 'n':
            if alimentacaoRuim == 's':
              print ('atenção!')
            else:
              print ('2 de 4, nada mal!')
          else:
            if alimentacaoRuim == 's':
              print ('No meio do caminho!')
            else:
              print ('Uau! 3 de 4!')
      else:
        if int(tempoDeTrabalho) > 6:
          if fazAtividadeFisica == 'n':
            if alimentacaoRuim == 's':
              print ('atenção!')
            else:
              print ('Não está ruim, mas pode melhorar!')
          else:
            if alimentacaoRuim == 's':
              print ('Quase lá! Melhora essa dieta!')
            else:
              print ('Quase fechou!!!')
        else:
          if fazAtividadeFisica == 'n':
            if alimentacaoRuim == 's':
              print ('Para melhorar só depende de você!')
            else:
              print ('É isso aí! Só falta se mexer!')
          else:
            if alimentacaoRuim == 's':
              print ('Já está chegando! Agora é só fechar a boca!')
            else:
              print ('Gostei de ver! Gabaritou!!!')
    else:
      print ('Escreveu errado.')
  else:
    print ('Escreveu errado.')
else:
  print ('Escreveu errado.')
