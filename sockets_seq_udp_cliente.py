import socket

#tamanho maximo de bytes
MAX_BYTES = 65535
#recebe o texto para enviar para o servidor
texto_para_enviar = input("Texto para enviar para o servidor: ")
#parametros para conexao com o servidor em tupla
#tupla nao permite que se altera depois
dados_do_servidor = ("127.0.0.1", 8080)
#dados para envio
dados = texto_para_enviar.encode("utf-8")

#Sock_DGRAM = UDP
#sempre o primeiro campo é AF_INET
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#envia o texto para o servidor
socket_cliente.sendto(dados, dados_do_servidor)

print("Mensagem enviada: ", texto_para_enviar)
#primeiro recebe a mensagem e o segundo o ip da resposta
dados, endereco = socket_cliente.recvfrom(MAX_BYTES)
#converte o bytes para string (texto)
texto_de_reposta = dados.decode("utf-8")
print("O servidor {}:{} respondeu '{}'".format(
    endereco[0], endereco[1], texto_de_reposta))
