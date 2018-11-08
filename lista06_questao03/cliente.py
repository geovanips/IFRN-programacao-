import arquivo_cliente
import menu

while True:
    opcao = menu.ler_opcao()
    if opcao == 0:
        print("Saindo do programa...")
        break
    elif opcao == 1:
        arquivo_cliente.cadastrar()
    elif opcao == 2:
        arquivo_cliente.listar_cadastro()
    else:
        print("Opção inválida, tente novamente!")