'''Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
faça um programa que calcule o valor de H com N
termos. O valor N será digitado pelo usuário e
deverá ser maior que zero.'''
h=0
while True:
    n=int(input("Digite o valor de N maior que zero: "))
    if n== 0:
        print("Digite valores acima de zero")
    else:
        break
for i in range(1, n + 1):
    h += 1/i
    if i == 1:
        print("1", end="")
    else:
        print("1/{}".format(i), end="")
    if i != n:
        print(" + ", end="")
print(" = {}".format(h))
