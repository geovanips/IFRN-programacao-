#Modulo arquivo
#funções de salvar,listar e buscar contato

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
def buscar_contatos():
    contato=input("Digite o nome do contato: ")
    arquivo = open("contatos.txt", "r", encoding="utf-8")
    for linha in arquivo:
        # split quebra a alinha aonde estiver o caractere entre parenteses.
        campos = linha[:-1].split(";")
        if contato == campos[0]:
            print("Nome: ", campos[0])
            print("Telefone:", campos[1])
            print("Email:", campos[2])
            print("--------------------")
            # sempre ao abrir algum arquivo deve fechar
    arquivo.close()
