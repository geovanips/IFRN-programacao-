import sqlite3

conexao = sqlite3.connect("aula_banco_py.db")
c = conexao.cursor()

esp = input("Digite a especialidade: ")

c.execute("select id, nome, rg from medico where especialidade = ?", (esp,))
resultado = c.fetchall()

print("Médicos com especialidades: %s" % esp)
for linha in resultado:
    print("ID:", linha[0])
    print("Nome: ", linha[1])
    print("RG: ", linha[2])
    print("- - - - - - - - - - - -")

conexao.close()
