import math
def combination(n, r):
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)

print(combination(23,10))
num_of_more_than_million = 0
for n in range (23,101):
    for r in range(0, n):
        if combination(n, r) > 1000000:
            num_of_more_than_million+=1
print(num_of_more_than_million)