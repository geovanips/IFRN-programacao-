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

n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))
n3 = int(input("Digite a nota 3: "))
n4 = int(input("Digite a nota 4: "))

#encapsulamento dos dados
dados = struct.pack(comum.P_NOTAS, n1, n2, n3, n4)
#envia os dados para o servidor
socket_cliente.sendall(dados)
#recebe o resultado encapsulado
#calcsize analiza o tamanho necessario para o byte recebido
resultado = socket_cliente.recv(struct.calcsize(comum.P_RESULTADO))
#desencapsulamento do dado recebido em uma lista
res_unpack = struct.unpack(comum.P_RESULTADO, resultado)
#imprime a media e a situaçao recebido atraves do resultado
print("Média: %d." %res_unpack[0])
print("Situação: %s." % res_unpack[1].decode(comum.ENCODING))
#encerra a conexao
socket_cliente.close()
