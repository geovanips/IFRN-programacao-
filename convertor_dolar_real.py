#conversor de Real para Dolar ou vice-versa.
#cotacao USS 1= 3,25 reais
#cotacao R$ 1 = 0,30 dolar
opcao=input("Digite a opção (1) dolar para real ou (2) real para dolar: ")
if opcao == '1':
    num=int(input("Digite o valor USS que deseja converter: "))
    print("O valor em Reais é: " , num*3.25)
elif opcao == '2':
    num=int(input("Digite o valor R$ que deseja converter: "))
    print("O valor em Dolar é: " , num/3.25)
else:
    print("Opção invalida! Tente Novamente. ")
