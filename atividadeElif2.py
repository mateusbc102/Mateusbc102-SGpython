nota1 = float(input("Qual a sua nota da primeira prova? "))
nota2 = float(input("Qual a sua nota da segunda prova? "))
nota3 = float(input("Qual a sua nota da terceira prova? "))
media = ((nota1 + nota2 + nota3) / 3)

if media == 10:
  print ("Nota Perfeita, tirou A!")
elif media >= 9:
  print ("Aprovado, tirou A!")
elif media >= 8:
  print ("Aprovado, tirou B!")
elif media >= 7:
  print ("Aprovado, tirou C!")
elif media >= 6:
  print ("Aprovado, tirou D!")
elif media >= 5:
  print ("Aprovado, tirou F!")
else:
  print ("Reprovado, tirou F!")
