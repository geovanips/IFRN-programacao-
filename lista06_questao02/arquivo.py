import socket
def salvar_produtos(nome, preco, preco2):
    arquivo = open("quantidade.txt", "a", encoding="utf-8")
    arquivo.write("{};{};{}\n".format(nome, preco, preco2))
    arquivo.close()

def inicia_conexao():
    ip = "127.0.0.1"
    porta = 8080
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((ip, porta))
    return socket_cliente
