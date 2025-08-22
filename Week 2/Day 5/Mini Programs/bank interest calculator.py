import math

def compound_interest(principal, rate, time):
    return principal * (math.pow((1 + rate / 100), time))

p = 5000
r = 7
t = 3

print("Principal:", p)
print("Rate:", r, "%")
print("Time:", t, "years")

amount = compound_interest(p, r, t)
print("Compound Interest =", round(amount - p, 2))
