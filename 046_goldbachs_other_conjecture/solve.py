import math

class PrimeFinder:
    def __init__(self):
        self.primes = [2,3,5,7,11,13]
    
    def isPrime(self, num):
        if num > 20000:
            digit_sum = sum([int(c) for c in str(num)])
            if digit_sum % 3 == 0:
                return False
        sq = math.sqrt(num)
        for i in self.primes:
            if num % i == 0:
                return False
            if i > sq + 1:
                break
        return True
    
    def updatePrimeListTo(self, num):
        if self.primes[-1] > num:
            return
        for i in range(self.primes[-1] + 2, num + 1, 2):
            if i%10 == 5:
                continue
            if self.isPrime(i):
                self.primes.append(i)
    
    def printPrimes(self, withIndex=False):
        index = 1
        for i in self.primes:
            if withIndex:
                print(index, i)
            else:
                print(i)
            index+=1


def is_goldback_number(odd_num, primes):
    for p in primes:
        if p > odd_num:
            break
        half_diff = (odd_num - p) / 2
        sq = math.sqrt(half_diff)
        if sq == int(sq):
            return p, sq, True
    return 0, 0, False

if __name__ == "__main__":
    pf = PrimeFinder()
    pf.updatePrimeListTo(20000)
    pf.printPrimes(True)
    for i in range (35, 10000, 2):
        p, sq, isGold = is_goldback_number(i, pf.primes)
        if isGold:
            print("%d = %d + 2 * %d * %d" % (i, p, sq, sq))
        else:
            print("%d is not a goldbach number" % i)
            break
    
            