// Make sure you have a file called input_1 with a number on each line in the
// same directory from which you are executing.
package main

import (
	"fmt"
	"os"
	"strconv"
)
type convert func(string) int

func parsefunc(s string) int {
	buff, _ := strconv.Atoi(s)
	return buff
}

func sum(r []int) int {
	retval := 0
	for _, i := range r {
		retval += i
	}
	return retval
}

func contains(s []int, e int) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func main() {
	current_freq := 0
	previous_freqs := []int{0}
	freqs := readLines("../data/input_1", parsefunc).([]int)
	// Question 1
	fmt.Printf("Question 1: %d\n", sum(freqs))
	// Question 2
	for true {
		for _, freq := range freqs {
			current_freq += freq
			if contains(previous_freqs, current_freq) {
				fmt.Printf("Question 2: %d\n", current_freq)
				os.Exit(0)
			}
			previous_freqs = append(previous_freqs, current_freq)
		}
	}
}
