import menu
import arquivo

while True:
    #para chamar um modulo deve colocar o nomedoarquivo.funcao
    opcao = menu.ler_opcao()
    if opcao == 0:
        print("Saindo do programa...")
        break
    elif opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = int(input("Digite o nome do telefone: "))
        email = input("Digite o e-mail do contato: ")
        arquivo.salvar_contato(nome, telefone, email)
    elif opcao == 2:
        arquivo.listar_contatos()
    elif opcao == 3:
        arquivo.buscar_contatos()
    else:
        print("Opção invalida, tente novamente")
