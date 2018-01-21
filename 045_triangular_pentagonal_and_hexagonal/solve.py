def get_triangular(num):
    return num*(num+1) / 2

def get_pentagonal(num):
    return num*(3*num - 1) / 2

def get_hexagonal(num):
    return 2*num*num - num


if __name__ == "__main__":
    t_list, p_list, h_list = [], [], []
    for i in range(1, 56000):
        t_list.append(get_triangular(i))
        p_list.append(get_pentagonal(i))
        h_list.append(get_hexagonal(i))
    
    for t in t_list:
        if t in p_list and t in h_list:
            print(t)
