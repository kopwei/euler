import os

numbers = []
max_numbers = []

def get_max_loc(i, j):
    if max_numbers[i][j] != -1:
        return max_numbers[i][j]
    if(i == len(numbers) - 1):
        max_numbers[i][j] = numbers[i][j]
    else:
        x = get_max_loc(i+1, j)
        y = get_max_loc(i+1, j+1)
        max_numbers[i][j] = max([x,y]) + numbers[i][j]
    return max_numbers[i][j]

def get_max_sum():
    return get_max_loc(0, 0)


def main():
    
    with open(os.path.dirname(os.path.realpath(__file__)) + '/numbers.txt') as f:
        lines = f.readlines()
        for l in lines:
            numbers.append([int(n) for n in l.split(' ')])
    for i in range(len(numbers)):
        max_numbers.append([-1 for _ in numbers[i]])
    print(get_max_sum())
    #print(max_numbers)

if __name__ == '__main__':
    main()