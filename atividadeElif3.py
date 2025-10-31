idade = int (input("Qual sua idade? "))
autorização = (input("Tem autorização? (True/False): "))
ingresso = (input("Tem ingresso? (True/False): "))
vip = (input("Está na lista vip? (True/False): "))
if idade>= 18 and (ingresso == "True" or vip == "True"):
  print ("Adulto com ingresso liberado")
elif idade>= 12 and autorização == "True" and (ingresso == "True" or vip == "True"):
  print ("Pode guardar sua autorização e entrar")
else:
  print ("Entrada não permitida")
