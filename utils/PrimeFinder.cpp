//
// Created by ezhenwe on 2018-01-19.
//

#include "PrimeFinder.h"
#include <iostream>
#include <cmath>

using namespace std;

PrimeFinder::PrimeFinder(){
    static const int arr[] = {2,3, 5};
    for(int i = 0; i < 3; i++) {
        this->primes.push_back(arr[i]);
    }
}

bool PrimeFinder::isPrime(long long value){
    vector<long long>::const_iterator it = this->primes.begin();
    long long sqrt_val = static_cast<long long>(sqrt(value));
    for(; it != this->primes.end(); ++it) {
        if(*it >= sqrt_val + 3) break;
        if (value % *it == 0) {
            return false;
        }
    }
    return true;
}

void PrimeFinder::updatePrimeListUpTo(long long value){
    int num_of_primes = this->primes.size();
    if(this->primes[num_of_primes - 1] > value) {
        return;
    }
    for(int i = this->primes[num_of_primes - 1] + 2; i < value; i+=2) {
        if(i % 10 == 5) {
            continue;
        }
        if(this->isPrime(i)){
            this->primes.push_back(i);
        }
    }
    return;
}

void PrimeFinder::extendPrimeListTo(int number) {
    int num_of_primes = this->primes.size();
    if(num_of_primes >= number) return;
    for(long long i = this->primes[num_of_primes - 1] + 2; this->primes.size() < number; i+=2) {
        if(i % 10 == 5) {
            continue;
        }
        if(this->isPrime(i)){
            this->primes.push_back(i);
        }
    }
    return;
}

void PrimeFinder::printPrimes() {
    int num_of_primes = this->primes.size();
    cout << "Now we have " << num_of_primes << " primes in list" << endl;
    cout << "And they are:" << endl;
    vector<long long>::const_iterator it = this->primes.begin();
    for(int i = 1; it != this->primes.end(); i++, it++) {
        cout << i << "," << *it << endl;
    }
}

long long PrimeFinder::getSumOfPrimes() {
    long long sum = 0L;
    vector<long long>::const_iterator it = this->primes.begin();
    for(;it != this->primes.end(); it++) {
        sum += *it;
    }
    return sum;
}
