import socket
import struct
import comum
#Sockets TCP
ip = "127.0.0.1"
porta = 8080

#cria o socket TCP
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#informa ao cliente socket o ip e porta para conectar ao servidor
socket_cliente.connect((ip, porta))

quantidade = int(input("Digite a quantidade de produtos a ser cadastrados: "))

for i in range(1, quantidade + 1): #criando listas com produtos e preços nas duas lojas
    nome = input("Digite o nome do produto {}" .format(i))
    preco = float(input("Digite o preço do produto {} na loja 1: " .format(i)))
    preco2 = float(input("Digite o preço do produto {} na loja 2: ".format(i)))
    dados = struct.pack(comum.P_NUM, nome.encode(comum.ENCODING), preco, preco2)
    # envia os dados para o servidor
    socket_cliente.sendall(dados)
#encerra a conexao
socket_cliente.close()