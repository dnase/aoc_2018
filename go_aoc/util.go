package main

import (
	"bufio"
	"os"
)

func readLines(path string, parsefunc convert) interface{} {
	file, err := os.Open(path)
	if err != nil {
		return nil
	}
	defer file.Close()

	var lines []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		buff := parsefunc(scanner.Text())
		lines = append(lines, buff)
	}
	return lines
}
