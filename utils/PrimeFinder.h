//
// Created by ezhenwe on 2018-01-19.
//

#ifndef HELLOWORLD_PRIMEFINDER_H
#define HELLOWORLD_PRIMEFINDER_H

#include <vector>

using namespace std;

class PrimeFinder {
public:
    PrimeFinder();

    bool isPrime(long long value);

    void updatePrimeListUpTo(long long value);

    void extendPrimeListTo(int number);

    void printPrimes() ;

    long long getSumOfPrimes();
private:
    vector<long long> primes;
};

#endif //HELLOWORLD_PRIMEFINDER_H
