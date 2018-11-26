def cal_media(nota1, nota2, nota3, nota4):
    media = (nota1+nota2+nota3+nota4)/4
    return media

def situacao(media):
    if media >= 70:
        situacao = "aprovado"
    elif media < 30:
        situacao = "reprovado"
    else:
        situacao = "recuperacao"
    return situacao
contagem_ap = 0
contagem_rec = 0
contagem_rep = 0

def contagem(situacao):
    cont = []
    global contagem_ap, contagem_rec, contagem_rep
    if situacao == "aprovado":
        contagem_ap += 1
    elif situacao == "reprovado":
        contagem_rep += 1
    elif situacao == "recuperacao":
        contagem_rec += 1
    cont = [contagem_ap, contagem_rep, contagem_rec]
    return cont