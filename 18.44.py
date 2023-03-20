C1 = float(input("enter capacitance1: "))
C2 = float(input("enter capacitance2: "))
V = float(input("enter voltage: "))

Ceq = C1*C2/(C1+C2)
q = Ceq * V
print(q, "microC")

print(q, "microC")

V1 = q/C1
print(V1)

V2 = q/C2
print(V2)