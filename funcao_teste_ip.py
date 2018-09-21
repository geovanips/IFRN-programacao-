def validar_ip(ip):
    #Ao receber o ip iremos quebrar o ip recebido pelo . atraves do split
    partes = ip.split(".")
    p0 = int(partes[0])
    p1 = int(partes[1])
    p2 = int(partes[2])
    p3 = int(partes[3])
    return 0 <= p0 <= 255 and 0 <= p1 <= 255 and 0 <= p2 <= 255 and 0 <= p3 <= 255
while True:
    ip = input("Digite o endereço IP:")
    if ip == "sair":
        break
    if validar_ip(ip):
        print("O IP {} é valido".format(ip))
    else:
        print("O IP {} é invalido".format(ip))

