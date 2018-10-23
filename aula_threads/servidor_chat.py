import socket
import threading
ip = "0.0.0.0"
porta = 8080

#funcao que irar para a Threading, o que deixara o servidor
#realizar mais conexoes.
def tratar_cliente(socket_con, endereco_con):
    #recebendo o apelido
    apelido = socket_con.recv(1024).decode("utf-8")
    #O apelido conecotu comn o ip tal
    print("{} conectou como {}!".format(endereco_con, apelido))
    #while para tratar todas as mensagem do cliente
    while True:
        #recebe a mensagem do cliente
        msg = socket_con.recv(1024).decode("utf-8")
        #mostra em tela o apelido + a mensagem enviada
        print("{}: {}".format(apelido, msg))
        #se receber a mensagem sair, para encerrar a conexao
        if msg == "sair":
            break
    socket_con.close()

#cria um socket tcp "stream"
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#passados o parametros endereço ip e porta para conexao
socket_servidor.bind((ip, porta))
#maximo de conexões que o servidor recebera
socket_servidor.listen(20)

while True:
    #Esperando receber dados na porta informado para bind
    #Dados: conteudo recebido pelo servidor
    print("Esperando conexão...")
    #servidor ele fica esperando o cliente executar o connect
    #so libera depois da conexao
    socket_conexao, endereco_cliente = socket_servidor.accept()
    #Threading para tratar a conexao com o cliente, assim que chegar o cliente
    #ele trata o cliente e permite que o servidor receba uma proxima conexao.
    threading.Thread(target=tratar_cliente, args=(socket_conexao, endereco_cliente)).start()
