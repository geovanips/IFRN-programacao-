'''Lista de exercicio programacao para redes
Questao 3
Faça um programa que pergunte quanto você ganha por hora e
o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.'''
print("Calculo do salario do mes")
sph=float(input("Digite quanto recebe por hora trabalhada: "))
horas=int(input("Digite as horas trabalhadas no mes: "))
salario_mes=sph*horas
print("Seu salario será: R$","%.2f" % salario_mes)
