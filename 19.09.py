R1 = float(input('enter R1: '))
R2 = float(input('enter R2: '))
R3 = float(input('enter R3: '))

Req = R1 + 1/(1/R2 + 1/R3)

I = 18/Req
I2 = R3/(R2+R3) * I
I3 = R2/(R2+R3) * I
print(I)
print(I2)
print(I3)