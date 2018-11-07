def salvar_produtos(nome, preco, preco2):
    arquivo = open("quantidade.txt", "a", encoding="utf-8")
    arquivo.write("{};{};{}\n".format(nome, preco, preco2))
    arquivo.close()

