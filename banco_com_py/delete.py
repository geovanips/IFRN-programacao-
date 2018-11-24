import sqlite3

conexao = sqlite3.connect("aula_banco_py.db")
c = conexao.cursor()

rg = int(input("Digite o RG para remover a pessoa: "))

c.execute("delete from pessoa where rg = ?", (rg,))
print("Linhas removidas: ", c.rowcount)


conexao.commit()
conexao.close()
