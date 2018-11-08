def salvar_produtos(nome, preco, preco2):
    arquivo = open("quantidade.txt", "a", encoding="utf-8")
    arquivo.write("{};{};{}\n".format(nome, preco, preco2))
    arquivo.close()

def listar_produtos():
    p = []
    arquivo = open("quantidade.txt", "r", encoding="utf-8")
    for linha in arquivo:
        campos = linha[:-1].split(";")
        p.append(campos)
    arquivo.close()
    return p
