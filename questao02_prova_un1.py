#Avaliação: Programação para Redes
#Leonardo Felipe da Silva Soares
#Questão 2

#Lista de ips e dispositivos disponível no arquivo "ips.txt"
f = open("ips.txt", "r") #abrir arquivo em modo de leitura
b = f.read()
lista=b.split() #lista obtida através dos elementos separados por espaço
visto ={}
duplicados=[] #itens duplicados
c=0
for x in lista:
    if x not in visto: #verificar se item ja foi visto, se nao adicionalo na lista visto
        visto[x]=1
    else:
        if visto[x]==1: #caso contrario se tiver sido visto haverá algum confito e o ip sera adicionado ao duplicados
            c=c+1
            duplicados.append(x)
if c > 0: #se houver conflito
    print("Existe conflito para os IPs:")
    for s in duplicados: #itens duplicados
        print(s)
elif c==0: #se nao houver conflito
    print("Não existe conflito entre IPs")

f.close()