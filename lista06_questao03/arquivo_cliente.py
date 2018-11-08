import socket
import struct
import comum
def cadastrar():
    id = 1
    ip = "127.0.0.1"
    porta = 82
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((ip, porta))
    request = struct.pack(comum.p_request, id)
    socket_cliente.sendall(request)
    quantidade = int(input("Digite a quantidade de produtos a ser cadastrados: "))
    quantidade_pack = struct.pack(comum.p_quantidadeProduto, quantidade)
    socket_cliente.sendall(quantidade_pack)
    for i in range(quantidade):
        produto = input("Digite o nome do produto {}: ".format(i + 1))
        precolj01 = float(input("Digite o preço do produto {} na loja 1: ".format(produto)))
        precolj02 = float(input("Digite o preço do produto {} na loja 2: ".format(produto)))
        dados = struct.pack(comum.P_NUM, produto.encode(comum.ENCODING), precolj01, precolj02)
        socket_cliente.sendall(dados)
    socket_cliente.close()
def listar_cadastro():
    id = 2
    ip = "127.0.0.1"
    porta = 82
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((ip, porta))
    request = struct.pack(comum.p_request, id)
    socket_cliente.sendall(request)
    while True:
        resposta = socket_cliente.recv(struct.calcsize(comum.p_resposta))
        resposta_unpack = struct.unpack(comum.p_resposta, resposta)
        print('Nome do Produto: {}'.format(resposta_unpack[0].decode(comum.ENCODING)))
        print('Preço na Loja 1 R${} e na loja 2 R${}'.format(resposta_unpack[1], resposta_unpack[2]))
        print('Preço Mais Barato do Produto R$:{}'.format(resposta_unpack[3]))
        print('Preço Mais Caro do Produto R$:{}'.format(resposta_unpack[4]))
        print('Preço Médio do Produto: {}'.format(resposta_unpack[5]))

    socket_cliente.close()
