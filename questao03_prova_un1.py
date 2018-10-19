#Avaliação: Programação para Redes
#Leonardo Felipe da Silva Soares
#Questão 3

texto = input("Digite o texto a ser verificado a quantidade de repetições: ")
lista = texto.split() #lista obtida pelos elementos separados por espaço
Lower = [item.lower() for item in lista]
palavras_unicas = set(Lower)
for palavras in palavras_unicas:
    print(' A palavra "{}" aparece {} vezes.'.format(palavras,Lower.count(palavras)))