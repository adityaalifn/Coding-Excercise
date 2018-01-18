package main

import (
	"fmt"
	"sort"
)

func main() {
	test := []int{4, 2, 3, 1, 5}
	fmt.Println(Solution(test))
}

func Solution(A []int) int {
	// n := len(A)
	// result := n * (n + 1) / 2
	// count := 0
	// for _, angka := range A {
	// 	count += angka
	// }

	// if count == result {
	// 	return 1
	// }
	// return 0
	A = sort.Ints(A)
	list := make([]int, )
	if A == range(1, len(A)+1){
		return 1
	}
	return 0
}
