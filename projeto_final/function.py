import sqlite3

bancoDeDados = 'database/contatos.db'

#adicionarContato
def inserirContato(contato):
    nome, sobrenome, celular, email, aniversario = contato.values()

    with sqlite3.connect(bancoDeDados) as conexao_db:
        cursor = conexao_db.cursor()

        cursor.execute("SELECT celular, email from contatos WHERE celular = ? OR email = ?;", (celular, email))
        dadosDoContato = cursor.fetchone()

        if dadosDoContato == None:
            cursor.execute("INSERT INTO contatos (nome, sobrenome, celular, email, aniversario) VALUES (?, ?, ?, ?, ?);", (nome, sobrenome, celular, email, aniversario))
            conexao_db.commit()
            return {'sucesso': 'O contato foi salvo!'}
        else:
            celularContato, emailContato = dadosDoContato

            if celularContato == celular and emailContato == email:
                return {'insucesso': 'O celular e o email já existe na agenda!'}
            elif celularContato == celular:
                return {'insucesso': 'O celular já existe na agenda!'}
            elif emailContato == email:
                return {'insucesso': 'O email já existe na agenda!'}


#consultarContato
def buscarContato(nome):
    with sqlite3.connect(bancoDeDados) as conexao_db:
        cursor = conexao_db.cursor()
        #cursor.execute("SELECT nome, sobrenome, email from contatos WHERE nome LIKE ? OR email = ?;", (nome,nome, ))
        cursor.execute("SELECT * from contatos WHERE nome LIKE '%{}%' OR email = '%{}%';".format(nome, nome))
        dadosDoContato = cursor.fetchall()
        print(dadosDoContato)
        if dadosDoContato == None:
            return {'insucesso': 'O contato não foi encontrado na agenda!'}
        else:
            agenda = []
            for contato in dadosDoContato:
                id, nome, sobrenome, celular, email, aniversario = contato
                agenda.append({"nome": nome, "sobrenome":sobrenome, "celular":celular, "email":email, "aniversario":aniversario})
            return agenda
#removerContato

def removerContato(email):
    with sqlite3.connect(bancoDeDados) as conexao_db:
        cursor = conexao_db.cursor()
        try:
            cursor.execute("delete from contatos where email = '{}'".format(email))
            conexao_db.commit()
            return {'sucesso': 'O contato foi removido'}
        except sqlite3.Error as erro:
            print(erro)
            return {'insucesso': 'Contato não foi removido'}
