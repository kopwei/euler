a = range(1,101)
b = [i * i for i in a]
print(sum(a) * sum(a) - sum(b))