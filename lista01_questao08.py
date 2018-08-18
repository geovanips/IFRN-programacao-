'''Lista de exercicio programacao para redes
Questao 8
Faça um programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total
do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:
a. Salário bruto;
b. Quanto pagou ao INSS;
c. Quanto pagou ao sindicato;
d. O salário líquido.
'''
def curto(num):
    return "%.2f" % num
print("Programa calculo do contracheque")
sph=float(input("Digite quanto recebe por hora trabalhada: "))
horas=int(input("Digite as horas trabalhadas no mes: "))
salario_bruto=sph*horas
d_inss=salario_bruto*0.08
d_leao=salario_bruto*0.11
d_sind=salario_bruto*0.05
salario_liq=salario_bruto-d_inss-d_leao-d_sind
print("Salario bruto: R$",curto(salario_bruto))
print("Desconto INSS: R$",curto(d_inss))
print("Desconto Imposto de Renda: R$",curto(d_leao))
print("Desconto do sindicato: ,R$", curto(d_sind))
print("Salario Liquido: R$",curto(salario_liq))
