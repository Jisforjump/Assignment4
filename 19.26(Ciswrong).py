R1 = float(input("enter R1 (in MΩ): ")) * 10**6
V1 = float(input("enter V1: "))
R2 = float(input("enter R2: "))
V2 = float(input("enter V2: "))

print(V1)

Vdiff = V1 - V2
I=V2/R2
R3 = Vdiff/I
print(R3)

##V3=V1/(R3+R2) * 7.1
##print(V3)

Vt = 7.1* V1/(7.1+R3)
print(Vt)