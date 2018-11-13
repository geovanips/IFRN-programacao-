def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ''
    return binario

mensagem = input("Digite sua mensagem")
binario = str_to_bin(mensagem)
print(binario)
