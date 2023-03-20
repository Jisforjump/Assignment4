l = float(input("enter distance: ")) * 1000
r = float(input("enter diameter: ")) /2 * 10**(-2)
I = float(input("enter current: "))

A = 3.14 * r**2
p = 1.72 * 10 ** (-8)
V = I * p * l /A
print(V)