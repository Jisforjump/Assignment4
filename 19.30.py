import math
R = float(input("enter R1: ")) * 1000
P = float(input("enter P1: "))

I = math.sqrt(P/R)
print(I)

V = math.sqrt(P*R)
print(V)

R2 = float(input("enter R2: ")) * 1000
V2 = float(input("enter V2: "))

P2 = V2 **2 /R2
print(P2)