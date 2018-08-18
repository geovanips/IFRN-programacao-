n1 = float(input("Digite a nota n1: "))
n2 = float(input("Digite a nota n2: "))
n3 = float(input("Digite a nota n3: "))
n4 = float(input("Digite a nota n4: "))
faltas = int(input("Digite a quantidade de faltas: "))
media = ((2 * n1) + (2 * n2) + (3 * n3) + (3 * n4)) / 10
if media >= 6 and faltas <= 15:
    print("Sua media foi:", "%.2f" % media, "Aluno aprovado!")
else:
    print("Sua media foi:", "%.2f" % media, "Aluno reprovado!")