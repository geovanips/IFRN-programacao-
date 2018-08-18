n1 = float(input("Digite a nota n1: "))
n2 = float(input("Digite a nota n2: "))
faltas = int(input("Digite a quantidade de faltas: "))
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