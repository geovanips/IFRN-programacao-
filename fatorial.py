while True:
  n=int(input("Digite um numero inteiro:"))
  if 0 <= n <= 12:
    break
  else:
    print("Digite entre 0 e 12")
fatorial=1
for i in range(n,1,-1):
  fatorial*=i
print("{}! = {}".format(n, fatorial))
