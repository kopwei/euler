def find_num():
    p_list = []
    for i in range(1, 50000):
        p_list.append(i * (3*i - 1) / 2)
    p_set = set(p_list)
    for i in range(len(p_set)):
        for j in range(i+1, len(p_set)):
            if (p_list[j] - p_list[i]) in p_set and p_list[j] + p_list[i] in p_set:
                print(p_list[j] - p_list[i])
                return i, j

find_num()