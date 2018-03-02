import math
#Determine 2 raizes de uma equação do 2º grau Y=a^2 + b + c.
a = int(input("Digite A: "))
b = int(input("Digite B: "))
c = int(input("Digite C: "))
#Calcula o delta
delta = int(((b**2) - (4 * a * c)))
#Calcula o x1
x1 = int((((-b) + (math.sqrt(delta)))/(a*2)))
#Calcula o x2
x2 = int((((-b) - (math.sqrt(delta)))/(a*2)))
print("As raizes são x1: " + str(x1) +" e x2: " + str(x2))
