import struct
import socket
import comum
import arquivo
import threading
ip = "0.0.0.0"
porta = 82
# cria um socket tcp "stream"
def tratar_cliente(socket_con, endereco_con):
    print("Conexao Realizada")
    print("Esperando pacotes")
    id = socket_con.recv(struct.calcsize(comum.p_request))
    id_unpack = struct.unpack(comum.p_request, id)
    if id_unpack[0] == 1:
        quantidadep = socket_con.recv(struct.calcsize(comum.p_quantidadeProduto))
        quantidadep_unpack = struct.unpack(comum.p_quantidadeProduto, quantidadep)
        quantidade_produto = quantidadep_unpack[0]
        print("Serão cadastrados {} produtos, atraves do cliente{}".format(quantidade_produto, endereco_con))
        for i in range(quantidade_produto):
            dados = socket_conexao.recv(struct.calcsize(comum.P_NUM))
            dados_unpack = struct.unpack(comum.P_NUM, dados)
            produto = dados_unpack[0].decode(comum.ENCODING)
            precoLoja01 = dados_unpack[1]
            precoLoja02 = dados_unpack[2]
            arquivo.salvar_produtos(produto, precoLoja01, precoLoja02)
            print("Produto {} foi cadastrado".format(produto))
        socket_con.close()
    elif id_unpack[0] == 2:
        tabela = arquivo.listar_produtos()
        if len(tabela) == "":
            print("Tabela sem cadastro")
        for i in range(len(tabela)):
            r_produto = (tabela[i][0].split('\x00', 1)[0])
            r_pl01 = float(tabela[i][1])
            r_pl02 = float(tabela[i][2])
            r_barato = min(r_pl01, r_pl02)
            r_caro = max(r_pl01, r_pl02)
            media = (r_pl01 + r_pl02) / 2
            resposta_pack = struct.pack(comum.p_resposta, r_produto.encode(comum.ENCODING), r_pl01, r_pl02, r_barato, r_caro, media)
            socket_con.sendall(resposta_pack)
        socket_con.close()
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind((ip, porta))
socket_servidor.listen(10)
while True:
    print("Esperando conexão...")
    socket_conexao, endereco_cliente = socket_servidor.accept()
    threading.Thread(target=tratar_cliente, args=(socket_conexao, endereco_cliente)).start()
