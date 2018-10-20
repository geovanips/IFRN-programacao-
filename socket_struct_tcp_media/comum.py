ENCODING = "utf-8"
#struct
#a exclação indica que é um pacote
#informa que terá 4 inteiros
P_NOTAS = "!i i i i"
#pacote de rede que encapsula 1 inteiro e 13bytes
P_RESULTADO = "!i 13s"  #len("Recuperação".encode("utf-8"))
