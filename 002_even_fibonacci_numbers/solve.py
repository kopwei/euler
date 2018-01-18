#!/usr/bin/python

def gen_fibonacci_list():
	fibo = [1,2,3,5]
	even_sum = 2
	for i in range(100):
		fibo.append(fibo[-1] + fibo[-2])
		if fibo[-1] < 4000000 and fibo[-1] % 2 == 0:
			even_sum += fibo[-1]
		if fibo[-1] > 4000000:
			break
	print(even_sum)
	return fibo

if __name__ == "__main__":
	print(gen_fibonacci_list())
		