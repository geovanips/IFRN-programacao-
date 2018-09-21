import socket

MAX_BYTES = 65535
#Aqui temos uma tupla: lista que não modifica
dados_para_bind = ("0.0.0.0", 8080) #IP, porta

#Cria um socket para usar IPV4(AF_INET) e UdP(SOCK_DGRAM)
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#fas o bind no IP 0.0.0.0 e porta 8080

#Fas o bind no IP 0.0.0.0 e porta 8080
#Reserva de porta
socket_servidor.bind(dados_para_bind)

while True:
    #Esperando receber dados na porta informado para bind
    #Dados: conteudo recebido pelo servidor
    #Endereço: informações (IP, porta) de q8em mandou os dados
    print("Esperando cliente...")
    dados, endereco = socket_servidor.recvfrom(MAX_BYTES)

    #Transforma os dados recebidos de bytes para texto
    texto_recebido = dados.decode("utf-8")
    #Mostra as informaçoes recebidas
    print("Recebido {} de {}:{}".format(texto_recebido, endereco[0], endereco[1]))

    #Preparando a resposta
    resposta_para_enviar = "Foram recebidos {} caracteres".format(len(texto_recebido))
    dados = resposta_para_enviar.encode("utf-8")

    #Enviando a resposta
    socket_servidor.sendto(dados, endereco)