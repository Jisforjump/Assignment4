r = float(input('enter diameter: ')) /2000
I = float(input('enter current: ')) / 1000
L = float(input('enter length: '))

p = 1.72 * 10**(-8)

A = 3.14*r**2
R = p * L / A
V = I*R
print(V)

pAg = 1.47*10**(-8)
RAg = pAg * L / A
VAg = I*RAg
print(VAg)