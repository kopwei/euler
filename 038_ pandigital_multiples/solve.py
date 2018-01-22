def is_pandigital_num(num):
    if len(num) != 9:
        return False
    s = str(num)
    n_list = [int(c) for c in s]
    n_list.sort()
    return n_list == [1,2,3,4,5,6,7,8,9]

pandigital_nums = []
for i in range (1, 50000):
    num_str = str(i)
    for j in range(2,6):
        num_str += str(i * j)
        if is_pandigital_num(num_str):
            pandigital_nums.append(num_str)

print(pandigital_nums)
