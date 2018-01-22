def is_palindrom(s):
    if not s:
        return False
    if len(s) == 1:
        return True
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

# only odd number is considered due to no leading zeroes
palindrom_nums = []
for i in range(1,1000000, 2):
    if i % 10 == 0:
        continue
    if is_palindrom(str(i)):
        base2_i_str = format(i, 'b')
        if is_palindrom(base2_i_str):
            print(i)
            palindrom_nums.append(i)
print(sum(palindrom_nums))

