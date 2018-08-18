while True:
  n1 = float(input("Digite a nota n1: "))
  n2 = float(input("Digite a nota n2: "))
  if (n1 > 10 or n1 < 0) or (n2 > 10 or n2 < 0):
    print("Nota invalida, tente novamente")
  else:
    break
while True:
  faltas = int(input("Digite a quantidade de faltas: "))
  if(faltas>0):
    break
  else:
    print("Numero de faltas deve ser maior ou igual a 0")
media = ((2 * n1) + (3 * n2)) / 5
if media < 3 and faltas > 15:
    print("Aluno reprovado por media e faltas!")
elif media < 3:
    print("Aluno reprovado por media")
elif faltas > 15:
    print("Aluno reprovado por faltas!")
elif media>=7:
    print("Sua media foi:", "%.2f" % media, "Aprovado")
else :
    print("Sua media foi:", "%.2f" % media, "Em recuperacao")