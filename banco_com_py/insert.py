import sqlite3

conexao = sqlite3.connect("aula_banco_py.db")
c = conexao.cursor()

cpf = input("Digite o CPF da pessoa: ")
rg = int(input("Digite o RG da pessoa: "))
nome = input("Digite o nome da pessoa: ")

c.execute("insert into pessoa(cpf, rg, nome) values (?, ?, ?)", (cpf, rg, nome))
print("Linhas inseridas: ", c.rowcount)


conexao.commit()
conexao.close
