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

n1 = int(input("Digite o numero: "))
n2 = int(input("Digite ouro numero: "))
print("Digite a operacao desejada")
print("+ = Soma")
print("- = Subtracao")
print("/ = Divisao")
print("x = Multiplicacao")
op = input(">> ")
dados = struct.pack(comum.P_NUM, n1, op.encode(comum.ENCODING), n2)
#envia os dados para o servidor
socket_cliente.sendall(dados)
#recebe o resultado encapsulado
#calcsize analiza o tamanho necessario para o byte recebido
resultado = socket_cliente.recv(struct.calcsize(comum.P_RESULTADO))
#desencapsulamento do dado recebido em uma lista
res_unpack = struct.unpack(comum.P_RESULTADO, resultado)
resposta=res_unpack[0]
#imprime a media e a situaçao recebido atraves do resultado
print("Resultado: %d" %resposta)
#encerra a conexao
socket_cliente.close()