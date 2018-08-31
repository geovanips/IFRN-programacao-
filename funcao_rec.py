#fatorial não recursivo
def fatorial_for(n):
    fat=1
    for i in range(2,n+1):
        fat*=i
        return
#fatorial recursivo
def fatorial_rec(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fatorial_rec(n-1)
n=int(input("Digite um numero inteiro positivo:"))
print("Usando for:", fatorial_for(n))
print("Usando recurssão:", fatorial_rec(n))
