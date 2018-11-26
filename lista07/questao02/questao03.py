#conecta ao banco
import sqlite3
import function
conexao = sqlite3.connect('banco2.db')
c = conexao.cursor()

c.execute("select * from aluno ")
resultado = c.fetchall()
soma_media = 0
for linha in resultado:
    print("Aluno {}: {}".format(linha[0], linha[1]))
    print("Curso: {}".format(linha[2]))
    print("Notas: {} {} {} {}".format(linha[3], linha[4], linha[5], linha[6]))
    media = function.cal_media(linha[3], linha[4], linha[5], linha[6])
    situacao = function.situacao(media)
    soma_media = soma_media + media
    print("Situacao: {} com media {}".format(situacao, media))
    contagem = function.contagem(situacao)
media_geral = soma_media/len(resultado)
c.execute("select count(*) from aluno")
total = c.fetchone()
print("Numero total de alunos: {}".format(total[0]))
print("Numero de alunos aprovados: {}".format(contagem[0]))
print("Numero de alunos em recuperacao: {}".format(contagem[2]))
print("Numero de alunos reprovados: {}".format(contagem[1]))
print("Média Geral da turma: {}".format(media_geral))