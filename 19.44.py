R1 = float(input("enter R1: "))
R2 = float(input("enter R2: "))
R3 = float(input("enter R3: "))
V = float(input("enter Volts: "))

Req = 1/ (1/R1 + 1/R2 + 1/R3)
print(Req, "Ω")

I1 = V/R1
I2 = V/R2
I3 = V/R3
print(I1, I2, I3)

I = V/Req
print(I)

print(V, V, V)

P1=V*V/R1
P2=V*V/R2
P3=V*V/R3
print(P1,P2,P3)

print("Since  P=V2/R and  V is the same for all three resistors, the resistor with the smallest  R dissipates the greatest power.")