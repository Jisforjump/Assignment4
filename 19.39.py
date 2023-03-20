import math
P = float(input("enter Power: "))
V = float(input("enter Volts: "))

R = V**2 / P
print(R)

I = math.sqrt(P/R)
print(I)

P1 = 11**2 / R
print(P1)