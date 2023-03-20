k = float(input("enter constant: "))
E = float(input("enter dielectric strength: ")) * 10**6
C = float(input("enter capacitance: ")) * 10 ** (0-9)
V = float(input("enter potential difference: ")) * 1000

d = V/E
A = C*d / (k*8.85*10**(-12))
print(A)