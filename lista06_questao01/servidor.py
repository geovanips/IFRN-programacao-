import struct
import socket
import comum

ip = "0.0.0.0"
porta = 8080
# cria um socket tcp "stream"
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind((ip, porta))
socket_servidor.listen(2)
while True:
    socket_conexao, endereco_cliente = socket_servidor.accept()
    print("Conexao Realizada")
    print("Esperando pacotes para realizar operacoes")
    dados = socket_conexao.recv(struct.calcsize(comum.P_NUM))
    dados_unpack = struct.unpack(comum.P_NUM, dados)
    op = dados_unpack[1].decode(comum.ENCODING)
    if op == "+":
        operacao = dados_unpack[0] + dados_unpack[2]
    elif op == "-":
        operacao = dados_unpack[0] - dados_unpack[2]
    elif op == "/":
        operacao = dados_unpack[0] / dados_unpack[2]
    elif op == "x":
        operacao = dados_unpack[0] * dados_unpack[2]
    else:
        operacao = 0
    resposta = struct.pack(comum.P_RESULTADO, operacao)
    socket_conexao.sendall(resposta)
socket_conexao.close()
