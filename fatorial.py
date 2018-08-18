n=-1
while (n > 12 or n < 0):
  n=int(input("Digite um numero inteiro:"))
fatorial=1
for i in range(n,1,-1):
  fatorial=fatorial*i
print(fatorial)
