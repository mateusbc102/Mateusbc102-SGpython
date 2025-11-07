idade = float(input('Qual a sua idade? '))
documento = input('Tem RG ou CNH? (s/n) ')
cartao = input('Posssui cartao de debito? (s/n) ')
aplicativo = input('Possui aplicativo? (s/n) ')
senha_4_digitos = input('Possui senha de 4 digitos? (s/n) ')
biometria = input('Possui biometria cadastrada na conta? (s/n) ')
senha_6_digitos = input('Possui senha de 6 digitos? (s/n) ')
especie = input('Deseja dinheiro em especie? (s/n) ')
if idade >= 80 and documento == 's' and especie == 's':
    print ('Senhor(a) pode pegar a senha para se dirigir ao caixa convencional.')
elif especie == 'n' and (aplicativo == 's' and senha_4_digitos == 's'):
    print('Senhor(a) gentileza realizar a transacao pelos canais digitais.')
elif (cartao == 's' and biometria =='s') or (biometria == 's' and senha_6_digitos =='s') or (cartao =='s' and aplicativo =='s' and senha_4_digitos == 's' and senha_6_digitos =='s'):
    print ('Senhor(a) gentileza realizar a transacao no caixa eletronico')
elif documento == 's' and especie =='s':
    print ('Pode se dirigir para o atendimento no caixa')
else:
    print ('Infelizmente nao podemos antender o Senhor(a)')
