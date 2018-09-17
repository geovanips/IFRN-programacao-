"""
Modo de abertura para arquivos:
r -> apenas leitura
w -> escrita, mas apaga conteúdo existente
a -> escrita, mas nao apaga o conteudo
"""
while True:

  if opcao == 0:
    print("Saindo do programa...")
    break
  elif opcao == 1:
    nome = input("Digite o nome do contato: ")
    telefone = int(input("Digite o nome do telefone: "))
    email = input("Digite o e-mail do contato: ")
    arquivo = open("contatos.txt", "a", encoding="utf-8")
    arquivo.write("{};{};{}\n".format(nome, telefone, email))
    arquivo.close()
  elif opcao == 2:
    #utilizar a codificação utf-8
    arquivo = open("contatos.txt", "r", encoding="utf-8")
    #ler varias linhas do arquivo
    #arquivo.readlines()
    #podemos utilizar for par ler o readlines
    #for linha in arquivo.readlines():
    for linha in arquivo:
        #split quebra a alinha aonde estiver o caractere entre parenteses.
        campos = linha[:-1].split(";")
        print("Nome: ", campos[0])
        print("Telefone:", campos[1])
        print("Email:", campos[2])
        #sempre ao abrir algum arquivo deve fechar
    arquivo.close()
  else:
    print("Opção invalida, tente novamente")