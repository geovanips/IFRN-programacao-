import struct
import socket
import comum
import threading
ip = "0.0.0.0"
porta = 8080

#funcao que irar para a Threading, o que deixara o servidor
#realizar mais conexoes.
def tratar_cliente(socket_con, endereco_con):
    print("Conexao Realizada")
    print("Esperando pacotes de notas")
    # recebe as notas do cliente com o tamanho do P_notas
    # a função calcsize
    dados = socket_con.recv(struct.calcsize(comum.P_NOTAS))
    # o pacote dados é desenpacotado em notas
    notas = struct.unpack(comum.P_NOTAS, dados)
    # calculo da media
    media = (notas[0] + notas[1] + notas[2] + notas[3]) // 4

    if media >= 60:
        situacao = "Aprovado"
    elif media < 20:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"
    # envia a resposta em um pacote
    # P_RESULTADO tera media e situação
    # situação deve ser enviada codificada em utf 8
    resposta = struct.pack(comum.P_RESULTADO, media, situacao.encode(comum.ENCODING))
    socket_con.sendall(resposta)
    # encerra a conexao
    socket_con.close()

#cria um socket tcp "stream"
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#passados o parametros endereço ip e porta para conexao
socket_servidor.bind((ip, porta))
#maximo de conexões que o servidor recebera
socket_servidor.listen(10)

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
