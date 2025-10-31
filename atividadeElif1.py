nota1 = float(input("Qual a sua nota da primeira prova? "))
nota2 = float(input("Qual a sua nota da segunda prova? "))
nota3 = float(input("Qual a sua nota da terceira prova? "))
media = ((nota1 + nota2 + nota3) / 3)
if media == 10:
  print ("Nota Perfeita")
elif media >= 5:
  print ("Aprovado")
else:
  print ("Reprovado")
