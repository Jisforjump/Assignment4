C = float(input('enter capacitance: ')) * 10**(-12)
Q = float(input('enter charge: ')) *10**(-6)

V = Q/C
print(V)

V2 = 2*Q/C
print(V2)

W = 0.5 * Q * V * 1000
print(W)