// Make sure you have a file called input_1 with a number on each line in the
// same directory from which you are executing.
package main

import (
	"bufio"
	"fmt"
  "strings"
	"os"
	"strconv"
)

type rectangle struct {
  id string
  x int
  y int
  w int
  h int
}

type coordinate struct {
  x int
  y int
}

var pointmap map[coordinate]int

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		buff := scanner.Text()
		//if e != nil {
			// ???
		//} else {
			lines = append(lines, buff)
		//}
	}
	return lines, scanner.Err()
}

func get_rectangle(s string) rectangle {
  parts := strings.Split(s, " ")
  id      := strings.Replace(parts[0], "#", "", -1)
  coordparts  := strings.Split(parts[2], ",")
  dimparts    := strings.Split(parts[3], "x")
  x, _ := strconv.Atoi(coordparts[0])
  y, _ := strconv.Atoi(strings.Replace(coordparts[1], ":", "", -1))
  w, _ := strconv.Atoi(dimparts[0])
  h, _ := strconv.Atoi(dimparts[1])
  return rectangle{id: id, x: x, y: y, w: w, h: h}
}

func get_overlap(rectangles []rectangle) int {
  for _, r := range rectangles {
    for i := r.x; i < (r.x + r.w); i++ {
      for j := r.y; j < (r.y + r.h); j++ {
        pointmap[coordinate{x: i, y: j}] += 1
      }
    }
  }
  buff := 0
  for _, v := range pointmap {
    if v > 1 {
      buff += 1
    }
  }
  return buff
}

func get_no_overlap_id(rectangles []rectangle) string {
  for _, r := range rectangles {
    valid := true
    for i := r.x; i < (r.x + r.w); i++ {
      for j := r.y; j < (r.y + r.h); j++ {
        if pointmap[coordinate{x: i, y: j}] != 1 {
          valid = false
        }
      }
      if !valid {
        break
      }
    }
    if valid {
      return r.id
    }
  }
  return "hi"
}

func main() {
  pointmap = make(map[coordinate]int)
	seq, e := readLines("../data/input_3")
	if e != nil {
		fmt.Printf("failed to read file")
		os.Exit(3)
	}
  rectangles := []rectangle{}
  for _, s := range seq {
    rectangles = append(rectangles, get_rectangle(s))
  }
  fmt.Printf("Q1: %d\n", get_overlap(rectangles))
  fmt.Printf("Q2: %s\n", get_no_overlap_id(rectangles))
}
