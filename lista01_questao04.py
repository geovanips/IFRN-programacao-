'''Lista de exercicio programacao para redes
Questao 4
Faça um Programa que peça a temperatura em graus
Farenheit, transforme e mostre a temperatura
em graus Celsius'''
print("#Converta Farenheit para Celsius#")
farenheit=float(input("Digite a temperatura em Farenheit:"))
celsius= "%.2f" % ((5*(farenheit-32))/9)
print("A temperatura em Celsius sera:", celsius+"°")
