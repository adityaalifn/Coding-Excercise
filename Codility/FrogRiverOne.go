package main

import (
	"fmt"
)

func main() {
	arr := []int{1,3,1,4,2,3,5,4}
	fmt.Println(Solution(5, arr))
}

func Solution(X int, A []int) int {
	for idx, value := range A {
		if value >= X {
			return idx
		}
	}
	return -1
}
