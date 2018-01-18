#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


class PrimeFinder {
	public:
		PrimeFinder() {
			static const int arr[] = {2,3,5,7,11,13,17};
			for(int i = 0; i < 7; i++) {
				this->primes.push_back(arr[i]);
			}
		}
		void updatePrimeListUpTo(long long value){
			int num_of_primes = this->primes.size();
			if(this->primes[num_of_primes - 1] > value) {
				return;
			}
			for(int i = this->primes[num_of_primes - 1]; i < value; i+=2) {
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
			for(vector<int>::const_iterator it = this->primes.begin(); it != this->primes.end(); ++it) {
				cout << *it << endl;
			}
		}
		vector<int> getPrimeFactors(long long value) {
			vector<int> factors = vector<int>();
			for(vector<int>::const_iterator it = this->primes.begin(); it != this->primes.end(); ++it) {
				if(value % *it == 0) {
					factors.push_back(*it);
				}
				if(*it > sqrt(value)) break;
			}
			return factors;
		}
	private:
		bool isPrime(long long value) {
			for(vector<int>::const_iterator it = this->primes.begin(); it != this->primes.end(); ++it) {
				if (value % *it == 0) {
					return false;
				}		
			}
			return true;
		}
		vector<int> primes;
};

int main(int argc, char *argv[]) {
	PrimeFinder p = PrimeFinder();
	p.updatePrimeListUpTo(sqrt(600851475143L));
	vector<int> factors = p.getPrimeFactors(600851475143L);
	for(vector<int>::const_iterator it = factors.begin(); it != factors.end(); ++it) {
		cout << *it << endl;
	}
}