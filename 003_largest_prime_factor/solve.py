

class PrimeFinder:
    def __init__(self):
        self.primes_list = [2,3,5,7,11,13,17]

    def is_prime(self, val):
        for i in self.primes_list:
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

p = PrimeFinder()
#print(p.find_primes_up_to_val(int(600851475143 ** 0.5)))
print (p.find_prime_factors(600851475143))
