digit_dict = {1:'one', 2:'two', 3:'three',4:'four',5:'five',6:'six', 7:'seven',
            8:'eight', 9:'nine', 10:'ten',11:'eleven', 12:'twelve', 13:'thirteen',
            14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
            19:'nineteen'}
two_digits_dict = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
hundred = 'hundred'

def get_num_of_letters(val):
    if val < 20:
        return len(digit_dict[val])
    if val < 100:
        if val%10 ==0:
            return len(two_digits_dict[val])
        else:
            return len(two_digits_dict[val - val % 10]) + len(digit_dict[val % 10])
    if val < 1000 and val >= 100:
        basic_len = len(hundred) + len(digit_dict[int(val / 100)])
        if val % 100 != 0:
            basic_len += len('and')
            if val % 100 < 20:
                basic_len += len(digit_dict[val % 100])
            elif val % 10 == 0:
                basic_len += len(two_digits_dict[val % 100])
            else:
                basic_len += len(two_digits_dict[val % 100 - val % 10]) + len(digit_dict[val % 10])
        return basic_len
    else:
        return len('onethousand')

total = 0
for i in range(1, 1001):
    num = get_num_of_letters(i)
    print(i, num)
    total += num
print(total)