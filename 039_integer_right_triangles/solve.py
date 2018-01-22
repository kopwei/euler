import math

def find_possible_dimensions(total_len):
    dimensions = []
    for i in range(1, int(total_len / 2 + 1)):
        for j in range(int(total_len / 2 + 1) - i, int(total_len / 2 + 1)):
            if i + j > total_len:
                break            
            s = [i, j, total_len -i -j]
            s.sort()
            if s[0] == 0:
                continue
            if s[0] * s[0] + s[1] * s[1] == s[2] * s[2] and s not in dimensions:
                    dimensions.append(s)
    return dimensions


max_len = 0
max_i = 0
for i in range(10,1000):    
    dimensions = find_possible_dimensions(i)
    if dimensions:
        if len(dimensions) > max_len:
            max_len = len(dimensions)
            max_i = i
            print(dimensions)
print(max_i)