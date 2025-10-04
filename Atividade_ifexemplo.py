print ("Aluno: Qual o valor do docinho, meu chapa?")
preco = 3.50
querer = input ('Vendedor: O docinho está ' + str (preco) + ', vai querer, meu patrão? responda com "s" ou "n": ')
if querer == "s":
  print ('Vendedor: Quantos? ')
  quantidade = input ("Aluno: eu quero ")
  print ("Vendedor: Quantos reais voce tem ai?")
  carteira = input ('Aluno: Eu tenho ')
  if float (carteira) < preco * float (quantidade):
    print ('Vendedor: Cara, liso com liso escorrega, pega o beco!')
  if float (carteira) > preco * float (quantidade):
    carteira = float (carteira) - preco * float (quantidade)
    print ('Vendedor: Voce consegue comprar o que pediu e ainda sobra ' + str (carteira) + ' reais.')
  if float (carteira) == preco * float (quantidade):
    carteira = 0
    print ('Vendedor: Voce consegue comprar o que pediu e não sobra nada.')
if querer == "n":
  print ("Aluno: Vai roubar outro!")
