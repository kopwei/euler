package main

import (
	"fmt"
	"sync"
)

func get_triangular_number(i uint64) uint64 {
	return i * (i + 1) / 2
}

func get_num_of_factors(value uint64) int {
	num_of_factors := 1
	var i uint64
	for i = 2; i < value/2+1; i++ {
		if value%i == 0 {
			num_of_factors++
		}
	}
	return num_of_factors + 1
}

func get_result(i uint64, wg *sync.WaitGroup) int {
	num := get_num_of_factors(get_triangular_number(i))
	if num > 300 {
		fmt.Printf("value i is %d and factor nums are %d\n", i, num)
	}
	wg.Done()
	return num
}

// Result is 12375
func main() {
	//fmt.Println(get_num_of_factors(get_triangular_number(14399)))
	var i, j uint64
	var wg sync.WaitGroup
	for i = 100; i <= 14399; i += 8 {
		for j = 0; j < 8; j++ {
			wg.Add(1)
			go get_result(i+j, &wg)
		}
		wg.Wait()
	}
}
