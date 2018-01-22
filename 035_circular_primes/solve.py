import math
class PrimeFinder:
    def __init__(self):
        self.primes_list = [2,3,5,7,11,13,17]

    def is_prime(self, val):
        sqrt = math.sqrt(val)
        for i in self.primes_list:
            if i > sqrt + 1:
                break
            if val % i == 0:
                return False
        return True

    def find_primes_up_to_val(self, val):
        if self.primes_list[-1] > val:
            return self.primes_list
        for i in range(self.primes_list[-1], val, 2):
            if i % 10 == 5:
                continue
            if self.is_prime(i):
                #print(i)
                self.primes_list.append(i)
        return self.primes_list

    def find_prime_factors(self, val):
        ret = []
        for i in self.primes_list:
            if val % i == 0:
                print(i)
                ret.append(i)
        return ret

def is_circular_prime(p, all_primes):
    if p not in all_primes:
        return False
    s = str(p)
    for _ in range(len(s)):
        last_digit = p % 10
        # rotate
        p -= last_digit
        p /= 10
        p += last_digit * 10 ** (len(s) - 1)
        if p not in all_primes:
            return False


p = PrimeFinder()
p.find_primes_up_to_val(1000000)
for prime in p.primes_list:
    if is_circular_prime(prime, p.primes_list):
        print(prime)