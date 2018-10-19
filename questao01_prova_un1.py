#Avaliação: Programação para Redes
#Leonardo Felipe da Silva Soares
#Questão 1

n=int(input("Digite a quantidade de produtos a ser cadastrados:"))
loja1=[]
nomes=[]
loja2=[]

for i in range(1,n+1): #criando listas com produtos e preços nas duas lojas
    nome = input("Digite o nome do produto {}" .format(i))
    preco = float(input("Digite o preço do produto {} na loja 1" .format(i)))
    if 0 > preco or preco > 1000: #garantir que o preço esteja entre 1 e 1000
        print("Preço inválido")
        break
    preco2 = float(input("Digite o preço do produto {} na loja 2".format(i)))
    if 0 > preco2 or preco2 > 1000: #garantir que o preço esteja entre 1 e 1000
        print("Preço inválido")
        break
    loja1.append(preco)
    nomes.append(nome)
    loja2.append(preco2)

print("#################################")
for i in range(0, len(nomes)): #imprimir as informações de cada produto
    print("Nome do produto: {}".format(nomes[i]))
    print("Preços nas Duas Lojas: {:.2f} {:.2f}".format(loja1[i], loja2[i]))
    menor=loja1[i]
    maior=loja2[i]
    if loja2[i] < loja1[i]:
        menor=loja2[i]
        maior=loja1[i]
    print("Preço mais barato do produto: {:.2f}".format(menor))
    print("Preço mais caro do produto: {:.2f}".format(maior))
    print("Preço médio do produto: {:.2f}".format((loja1[i]+loja2[i])/2))
    print("\n#################################")


