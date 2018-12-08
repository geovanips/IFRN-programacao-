import sqlite3

bancoDeDados = 'database/contatos.db'
schema_db = 'sql/schema_db.sql'

with sqlite3.connect(bancoDeDados) as conexao_db:
    with open(schema_db, 'rt', encoding='UTF-8') as query:
        criar_schema_db = query.read()

    if conexao_db.executescript(criar_schema_db):
        print("A definição do banco de dados foi criado com sucesso.")
