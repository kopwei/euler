sum_val = 0
for i in range(3,1002, 2):
    sum_val += 4 * i*i - 6 * (i-1)
print(sum_val + 1)