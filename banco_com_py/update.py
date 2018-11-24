import sqlite3

conexao = sqlite3.connect("aula_banco_py.db")
c = conexao.cursor()

cpf = input("Digite o CPF da pessoa: ")
rg = int(input("Digite o novo RG da pessoa: "))
nome = input("Digite o novo nome da pessoa: ")

c.execute("update pessoa set nome = ?, rg = ? where cpf = ?", (nome, rg, cpf))
print("Linhas atualizadas: ", c.rowcount)


conexao.commit()
conexao.close()
