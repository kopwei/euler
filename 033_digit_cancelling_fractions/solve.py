def are_canceling_ok(numerator, denominator):
    n_list = [(numerator - numerator % 10) / 10, numerator%10]
    d_list = [(denominator - denominator % 10)/10, denominator % 10]
    if n_list[0] == d_list[1] and n_list[1] != d_list[0] and d_list[0] != 0:
        if n_list[1] / d_list[0] == numerator / denominator:
            return True
    if n_list[0] != d_list[1] and n_list[1] == d_list[0] and d_list[1] != 0:
        if n_list[0] / d_list[1] == numerator / denominator:
            return True
    return False

for i in range(10, 100):
    for j in range(i+1, 100):
        if are_canceling_ok(i, j):
            print(i, j)