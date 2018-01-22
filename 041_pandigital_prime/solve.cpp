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

	void printPrimes() {
		int num_of_primes = this->primes.size();
		cout << "Now we have " << num_of_primes << " primes in list" << endl;
		cout << "And they are:" << endl;
		vector<long long>::const_iterator it = this->primes.begin();
		for(int i = 1; it != this->primes.end(); i++, it++) {
			cout << i << "," << *it << endl;
		}
	}
private:
	vector<long long> primes;  
};

static vector<long long> big_numbers;
static int digits[7] = {1,2,3,4,5,6,7};

long long getBigNumber() {
	long long stage = 1;
	long long big_number = 0;
	for(int i = 0; i < 7; i++) {
		big_number += stage*(long long)(digits[i]);
		stage *= 10;
	}
	return big_number;
}

void swap(int i, int j) {
	int tmp = digits[i];
	digits[i] = digits[j];
	digits[j] = tmp;
}

void permute(int index) {
	if(index == 7) {
		big_numbers.push_back(getBigNumber());
	}
	for(int i = index; i < 7; i++) {
		swap(i, index);
		permute(index + 1);
		swap(index, i);
	}
}

int main(int argc, char *argv[]) {
	PrimeFinder p = PrimeFinder();
	p.extendPrimeListTo((int)sqrt(7654321L));
	permute(0);
	
	sort(big_numbers.begin(), big_numbers.end(), greater<int>());
	//std::reverse(big_numbers.begin(), big_numbers.end());
	vector<long long>::const_iterator it = big_numbers.begin();
	for(;it != big_numbers.end(); ++it) {
		if(*it % 2 == 0 || *it % 5 == 0) continue;
		if(p.isPrime(*it)) {
			cout << *it << endl;
		}
	}
	return 0;
}
