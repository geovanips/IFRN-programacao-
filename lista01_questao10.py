'''Lista de exercicio programacao para redes
Questao 10
Faça um Programa para uma loja de tintas. O programa
deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 6 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 3,6 litros, que custam R$ 25,00.'''
print("Calculo da quantidade de latas e preço da tinta")
area=float(input("Digite em m2 a area a ser pintada:"))
latas18=int(round(float(((area/6)/18) + 0.5)))
latas3=int(round(float(((area/6)/3.6) + 0.5)))
print("Quantidades de latas 18l a serem compradas:", latas18)
print("Preço total de latas 18l: R$",(latas18*80))
print("Quantidades de latas 3,6l a serem compradas:", latas3)
print("Preço total de latas 3,6l: R$",(latas3*25))
