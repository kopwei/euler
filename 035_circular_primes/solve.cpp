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
			//if(*it >= sqrt_val + 10) break; 
			if (value % *it == 0) {
				return false;
			}
		}
		return true;
	}
	void extendPrimeListTo(int number) {
		int num_of_primes = this->primes.size();
		if(num_of_primes >= number) return;
		for(long long i = this->primes[num_of_primes - 1]; this->primes.size() < number; i+=2) {
			if(i % 10 == 5) {
				continue;
			}
			if(this->isPrime(i)){
				this->primes.push_back(i);
			}
		}
		return;
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
             //cout << i <<endl;
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
    vector<long long> getPrimes() {
        return this->primes;
    }

private:
	vector<long long> primes;  
};


bool is_circular_prime(long long prime, vector<long long>& all_primes) {
    if(std::find(all_primes.begin(), all_primes.end(), prime) == all_primes.end()) {
        return false;
    }
    // rotate
    long long new_prime = prime;
    long long len = static_cast<long long>(log10(prime));
    if (0 == len) {
        return true;
    }
    do {
        long long last_digit = new_prime%10;
        new_prime = (new_prime - last_digit) / 10 + last_digit * pow(10, len);
        if(std::find(all_primes.begin(), all_primes.end(), new_prime) == all_primes.end()) {
            return false;
        }
    } while(new_prime != prime);
    return true;
}

int main() {
    PrimeFinder p = PrimeFinder();
    p.updatePrimeListUpTo(1000000L);
    vector<long long> primes = p.getPrimes();
    vector<long long>::const_iterator it = primes.begin();
    int counter = 0;
    for(;it != primes.end();it++) {
        if(is_circular_prime(*it, primes)) {
            cout << *it << endl;
            counter++;
        }
    }
    cout << "There are total " << counter<< " circular primes." << endl;
}