'''Lista de exercicio programacao para redes
Questao 7
João é um pescador. Toda vez que ele traz um peso de peixes
maior que o estabelecido pelo regulamento de pesca do seu
estado (50 quilos), ele deve pagar uma multa de R$ 4,00 por
quilo excedente. João precisa que você faça um programa que
leia o peso de peixes e diga a quantidade excedente e o
valor da multa para tal quantidade.'''
print("Programa para calcular multa do kg peixe excedente")
print("Multa de R$ 4 pelo excedente")
kg_peixe=float(input("Digite o kg do peixe:"))
if kg_peixe>50 :
    multa=(kg_peixe-50)*4
    print("A multa será de: R$",multa)
else :
    ("Valor dentro do regulamento. Não houve multa")
