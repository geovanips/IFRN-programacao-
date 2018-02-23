import math
#Determine 2 raizes de uma equação do 2º grau Y=a^2 + b + c.
a = int(input("Digite A: "))
b = int(input("Digite B: "))
c = int(input("Digite C: "))
delta = int(((b**2) + (4 * a * c)))
x1 = int((((b**2) + (math.sqrt(delta)))/(a*2)))
x2 = int((((b**2) - (math.sqrt(delta)))/(a*2)))
print("As raizes são x1: " + str(x1) +" e x2: " + str(x2))
