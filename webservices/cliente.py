import requests

resultado2 = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios")
dados2 = resultado2.json()
for municipios in dados2:
    print("Nome: ", municipios["nome"])
    print("Microregiao: ", municipios["microrregiao"]["nome"])
    print("Mesorregiao ", municipios["microrregiao"]["mesorregiao"]["nome"])
    print("-----------------------------------")
resultado_post = requests.post("https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios")
dados_pos = resultado_post.json()

