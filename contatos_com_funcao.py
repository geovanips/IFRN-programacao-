"""
Modo de abertura para arquivos:
r -> apenas leitura
w -> escrita, mas apaga conteúdo existente
a -> escrita, mas nao apaga o conteudo
"""

def ler_opcao():
    print("Escolha sua opção:")
    print("0 - Sair do programa")
    print("1 - Cadastrar um novo contato")
    print("2 - Listar os contatos cadastrados")
    return int(input(">> "))
def salvar_contato(nomec , telefonec, emailc):
    arquivo = open("contatos.txt", "a", encoding="utf-8")
    arquivo.write("{};{};{}\n".format(nomec, telefonec, emailc))
    arquivo.close()
def listar_contatos():
    # utilizar a codificação utf-8
    arquivo = open("contatos.txt", "r", encoding="utf-8")
    # ler varias linhas do arquivo
    # arquivo.readlines()
    # podemos utilizar for par ler o readlines
    # for linha in arquivo.readlines():
    for linha in arquivo:
        # split quebra a alinha aonde estiver o caractere entre parenteses.
        campos = linha[:-1].split(";")
        print("Nome: ", campos[0])
        print("Telefone:", campos[1])
        print("Email:", campos[2])
        print("--------------------")
        # sempre ao abrir algum arquivo deve fechar
    arquivo.close()
while True:
    opcao = ler_opcao()
    if opcao == 0:
        print("Saindo do programa...")
        break
    elif opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = int(input("Digite o nome do telefone: "))
        email = input("Digite o e-mail do contato: ")
        salvar_contato(nome, telefone, email)
    elif opcao == 2:
        listar_contatos()
    else:
        print("Opção invalida, tente novamente")