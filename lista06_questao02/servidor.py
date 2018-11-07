import struct
import socket
import comum
import arquivo
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
    arquivo.salvar_produtos(dados_unpack[0].decode(comum.ENCODING), dados_unpack[1], dados_unpack[2])

socket_conexao.close()
