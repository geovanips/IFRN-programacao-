import requests
n1 = input("Digite o primeiro numero")
n2 = input("Digite o segundo numero")
resultado = requests.get("http://127.0.0.1:2223/operacoes/{}/{}".format(n1, n2))
dados = resultado.json()
print("Soma: ", dados["soma"])
print("Subtracao: ", dados["subtracao"])
print("Multiplicacao ", dados["multiplicacao"])
print("Divisao: ", dados["divisao"])
print("-----------------------------------")
resultado_post = requests.post("https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios")
dados_pos = resultado_post.json()

