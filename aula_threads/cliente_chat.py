import socket

#Sockets TCP
ip = "127.0.0.1"
porta = 8080
#cria o socket TCP
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#informa ao cliente socket o ip e porta para conectar ao servidor
socket_cliente.connect((ip, porta))
apelido = input("Digite seu apelido: ")
#envia para o servidor o apelido
socket_cliente.sendall(apelido.encode("utf-8"))
while True:
    msg = input("Digite seu texto: ")
    socket_cliente.sendall(msg.encode("utf-8"))
    if msg.lower() == "sair":
        break
socket_cliente.close()
