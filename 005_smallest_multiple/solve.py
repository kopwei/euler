def find_min_multiple():
    primes = [2,3,5,7,11,13,17,19]
    i = 1
    for p in primes:
        i *= p
    
    i *= 8 * 3
    return i

print(find_min_multiple())