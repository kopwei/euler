def get_digits_list(num):
    digits = [int(c) for c in str(num)]
    digits.sort()
    return digits

def is_required_num(num):
    digits_list = get_digits_list(num)
    for i in range(2, 7):
        if get_digits_list(num * i) != digits_list:
            return False
    return True


for i in range(1,142858):
    if is_required_num(i):
        print(i)