import requests
def adicionarContato():
    campos = [
        "nome",
        "sobrenome",
        "celular",
        "email",
        "aniversario"
    ]
    contato = {}
    for campo in campos:
        contato[campo] = input("Informe o {} do contato: ".format(campo))
    resposta = requests.get("http://127.0.0.1:83/adicionarContato/", json=contato).json()
    if resposta:
        for msg in resposta:
            print("Mensagem de {}: {}".format(msg, resposta[msg]))

def home():
    resposta = requests.get("http://127.0.0.1:83/").json()
    return resposta
def consultarContato():
    print("Digite nome ou email:")
    opcao = input(">>")
    resposta = requests.get("http://127.0.0.1:83/consultarContato/{}".format(opcao)).json()
    print("Contato(s):")
    for e in resposta:
        print("Nome: {} {}\n Celular: {}\n Email: {}\n Aniversario: {}".format(e["nome"], e["sobrenome"], e["celular"],
                                                                               e["email"], e["aniversario"]))
        print("------------------------")
def removerContato():
    email = input("Digite o email do contato para remover: ")
    resposta = requests.get("http://127.0.0.1:83/removerContato/{}".format(email)).json()
    if resposta:
        for msg in resposta:
            print("Mensagem de {}: {}".format(msg, resposta[msg]))
