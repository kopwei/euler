package main

import "fmt"

func getNextVal(val uint64) uint64 {
	if val%2 == 0 {
		return val / 2
	}
	return val*3 + 1
}

func getList(val uint64) []uint64 {
	if val == 1 {
		return []uint64{1}
	}
	list := make([]uint64, 1)
	list[0] = val
	currentVal := val
	var nextVal uint64
	for {
		nextVal = getNextVal(currentVal)
		list = append(list, nextVal)
		currentVal = nextVal
		if currentVal == 1 {
			break
		}
	}
	return list
}

func main() {
	maxLen := 0
	var i uint64
	for i = 10; i < 1000000; i++ {
		list := getList(i)
		if len(list) > maxLen {
			maxLen = len(list)
			fmt.Printf("Value %d gives us a longer list which size is %d\n", i, maxLen)
		}
	}
	//fmt.Printf("%v", getList(999999))
}
