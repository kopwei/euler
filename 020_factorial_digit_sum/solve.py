import math
res = str(math.factorial(100))
digits = [int(c) for c in res]
print(sum(digits))