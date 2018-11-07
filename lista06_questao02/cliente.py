import struct
import comum
import arquivo
#Sockets TCP

quantidade = int(input("Digite a quantidade de produtos a ser cadastrados: "))

for i in range(1, quantidade + 1): #criando listas com produtos e preços nas duas lojas
    cliente = arquivo.inicia_conexao()
    nome = input("Digite o nome do produto {}" .format(i))
    preco = float(input("Digite o preço do produto {} na loja 1: " .format(i)))
    preco2 = float(input("Digite o preço do produto {} na loja 2: ".format(i)))
    dados = struct.pack(comum.P_NUM, nome.encode(comum.ENCODING), preco, preco2)
    # envia os dados para o servidor
    cliente.sendall(dados)
    cliente.close()
#encerra a conexao
