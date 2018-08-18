'''Lista de exercicio programacao para redes
Questao 9
Faça um programa para uma loja de tintas. O programa
deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.
'''
print("Calculo da quantidade de latas e preço da tinta")
area=float(input("Digite em m2 a area a ser pintada:"))
latas=int(round(float(((area/3)/18) + 0.5)))
preco=latas*80
print("Quantidades de latas a serem compradas:", latas)
print("Preço total de: R$",preco)
