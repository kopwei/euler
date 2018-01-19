import math

def combination(m, n):
    if n > m:
        m, n = n, m
    prod = 1
    for i in range (m, n, -1):
        prod *= i
    return prod/math.factorial(n)

print(combination(40, 20))