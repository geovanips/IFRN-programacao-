import c_function


#menu da aplicação
resposta = c_function.home()
print(resposta['serviço'])
print(resposta['descrição'])
opcoes = {1: "Adicionar Contato", 2: "Consultar Contato", 3: "Remover Contato"}

while True:
    print("\nOpções:")
    print("0 - Encerrar o programa")
    for opcao in opcoes:
        print("{} - {}".format(opcao, opcoes[opcao]))

    escolha = int(input(">> "))

    if escolha in opcoes.keys():
        print("\n{}\n{}\n".format(opcoes[escolha], resposta['opções'][opcoes[escolha]]))

        if escolha == 1:
            c_function.adicionarContato()
        elif escolha == 2:
            c_function.consultarContato()
        elif escolha == 3:
            c_function.removerContato()

    elif escolha == 0:
        print("O programa foi encerrado.")
        break

    else:
        print("\nOpção invalida!")
