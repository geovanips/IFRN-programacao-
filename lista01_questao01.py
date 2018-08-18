'''Lista de exercicio programacao para redes
Questao 1
Faça um programa que peça as 4 notas bimestrais e
mostre a média aritmética entre elas'''
print("Calculo da Media, Portanto Digite as 4 notas")
n1 = float(input("Digite a nota da unidade 1: "))
n2 = float(input("Digite a nota da unidade 2: "))
n3 = float(input("Digite a nota da unidade 3: "))
n4 = float(input("Digite a nota da unidade 4: "))
media = (n1+n2+n3+n4)/4
print("A media é :", "%.2f" % media)
