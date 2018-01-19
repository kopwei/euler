#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class PrimeFinder {
public:
    PrimeFinder(){
        static const int arr[] = {2,3,5,7,11,13,17};
	    for(int i = 0; i < 7; i++) {
		    this->primes.push_back(arr[i]);
	    }
    }

    bool isPrime(long long value){
        vector<long long>::const_iterator it = this->primes.begin();
        long long sqrt_val = static_cast<long long>(sqrt(value));
        for(; it != this->primes.end(); ++it) {
            if(*it >= sqrt_val + 1) break; 
			if (value % *it == 0) {
				return false;
			}
		}
		return true;
    }

    void updatePrimeListUpTo(long long value){
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

    void extendPrimeListTo(int number) {
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

    void printPrimes() {
        int num_of_primes = this->primes.size();
        cout << "Now we have " << num_of_primes << " primes in list" << endl;
        cout << "And they are:" << endl;
        vector<long long>::const_iterator it = this->primes.begin();
        for(int i = 1; it != this->primes.end(); i++, it++) {
            cout << i << "," << *it << endl;
        }
    }

    long long getSumOfPrimes() {
        long long sum = 0L;
        vector<long long>::const_iterator it = this->primes.begin();
        for(;it != this->primes.end(); it++) {
            sum += *it;
        }
        return sum;
    }
private:
    vector<long long> primes;  
};

int main() {
    PrimeFinder p = PrimeFinder();
    p.updatePrimeListUpTo(2000000L);
    //p.printPrimes();
    cout << "Sum is "<<p.getSumOfPrimes() << endl;
}

