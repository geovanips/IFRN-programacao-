'''
Servidor:
Implemente um serviço web que armazena os contados em um banco de dados. Serão
disponibilizados serviços para consultar contados (por nome e por e-mail), adicionar novos
contados e remover contatos existentes informando o e-mail para chave da remoção. Nem o e-mail
nem o celular podem se repetir em contatos diferentes. As consultas por nome devem usar padrões
para retornar resultados que sejam similares ao parâmetro de busca digitado.
'''

import flask
from flask import json,Response
import function

app = flask.Flask("Agenda de contatos na nuvem")

@app.route("/")
def home():
    resposta = {
      "serviço": "AGENDA NA NUVEM",
      "descrição": "O serviço de agenda permite que você armazene seus contatos na nuvem. Cada contato é representado pelo seu nome, sobrenome, celular, e-mail e aniversário (data de nascimento do contato).",
      "opções": {
        "Adicionar Contato": "Informe os campos: nome, sobrenome, celular, email, aniversário (no formato YYYY-MM-DD)",
        "Consultar Contato": "Informe o nome ou e-mail",
        "Remover Contato": "Informe o e-mail para chave da remoção"
      }
    }

    json_string = json.dumps(resposta,ensure_ascii = False)
    json_resposta = Response(json_string,content_type="application/json; charset=utf-8")

    return json_resposta

@app.route("/adicionarContato/")
def adicionarContato():
    contato = flask.request.get_json()
    resposta = function.inserirContato(contato)

    return flask.jsonify(resposta)


@app.route("/consultarContato/<string:nome>")
def consultarContato(nome):
    resposta = function.buscarContato(nome)
    print(resposta)
    return flask.jsonify(resposta)

@app.route("/removerContato/<string:email>")
def removerContato(email):
    resposta = function.removerContato(email)
    return flask.jsonify(resposta)



app.run("0.0.0.0", 83)
