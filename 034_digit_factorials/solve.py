import math

def is_curious_number(num):
    if num < 10:
        return False
    s = str(num)
    digits = [int(c) for c in s]
    sum_val = 0
    for d in digits:
        sum_val += math.factorial(d)
        if sum_val > num:
            return False
    return sum_val == num

for i in range(10, 10000000):
    if is_curious_number(i):
        print(i)