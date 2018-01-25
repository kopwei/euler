def is_wanted_number(num):
    nums = [int(c) for c in str(num)]
    return num == sum(map(lambda x: x **5 , nums))

def main():
    sum_val = 0
    for i in range(10, 295245):
        if is_wanted_number(i):
            print(i)
            sum_val += i
    print(sum_val)

if __name__ == '__main__':
    main()