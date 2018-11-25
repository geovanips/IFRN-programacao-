#conecta ao banco
import sqlite3
conexao = sqlite3.connect('banco2.db')
c = conexao.cursor()
sair = 1;
while True:
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o nome do curso: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))
    c.execute("insert into aluno(nome, curso, nota1, nota2, nota3, nota4) values (?, ?, ?, ?, ?, ?)", (nome, curso, nota1, nota2, nota3, nota4))
    conexao.commit()
    if c.rowcount > 0:
        print("Dados insesridos com sucesso:")
    else:
        print("Dados nao inseridos ou modificados")
    print("Deseja inserir novos dados?")
    sair = int(input("Digite 0 para nao e 1 para sim: "))
    if sair == 0:
        break;
