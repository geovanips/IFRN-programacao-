import flask
#nome da aplicacao
app = flask.Flask("Calculadora")
#Rotas da url para redirecionamento
@app.route("/")
def sobre():
    return "Este é um serviço web de calculadora"

@app.route("/potencia/<int:num1>/<int:num2>")
def calcular_potencia(num1, num2):
    return str(num1 ** num2)
@app.route("/operacoes/<int:num1>/<int:num2>")
def operacoes_basicas(num1, num2):
    resultados= {
        "soma": num1 + num2,
        "subtracao": num1 - num2,
        "multiplicacao": num1 * num2,
        "divisao": num1 / num2
    }
    #converte em json
    return flask.jsonify(resultados)
#Roda a aplicacao
app.run("127.0.0.1", 2223)
