
def is_palindromic(val):
    s = str(val)
    if len(s) % 2 != 0:
        return False
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def find_largest_palindromic():
    largest_par = 10000
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            if is_palindromic(i * j):
                if largest_par < i * j:
                    largest_par = i * j
                    print(i, j)
    return largest_par


def main():
    print(find_largest_palindromic())

if __name__ == '__main__':
    main()