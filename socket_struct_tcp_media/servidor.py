import struct
import socket
import comum
ip = "0.0.0.0"
porta = 8080

#cria um socket tcp "stream"
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind((ip, porta))
socket_servidor.listen(2)

while True:
    #Esperando receber dados na porta informado para bind
    #Dados: conteudo recebido pelo servidor
    print("Esperando conexão...")
    #servidor ele fica esperando o cliente executar o connect
    #so libera depois da conexao
    socket_conexao, endereco_cliente = socket_servidor.accept()
    print("Conexao Realizada")
    print("Esperando pacotes de notas")
    #recebe as notas do cliente com o tamanho do P_notas
    #a função calcsize
    dados = socket_conexao.recv(struct.calcsize(comum.P_NOTAS))
    #o pacote dados é desenpacotado em notas
    notas =  struct.unpack(comum.P_NOTAS, dados)
    #calculo da media
    media = (notas[0] + notas[1] + notas[2] + notas[3]) // 4

    if media>=60:
        situacao = "Aprovado"
    elif media<20:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"
    #envia a resposta em um pacote
    #P_RESULTADO tera media e situação
    #situação deve ser enviada codificada em utf 8
    resposta = struct.pack(comum.P_RESULTADO, media, situacao.encode(comum.ENCODING))
    socket_conexao.sendall(resposta)
    #encerra a conexao
    socket_conexao.close()
