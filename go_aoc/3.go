// Make sure you have a file called input_1 with a number on each line in the
// same directory from which you are executing.
package main

import (
	"fmt"
  "strings"
	"strconv"
)

type rectangle struct {
  overlap bool
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


func get_rectangle(s string) rectangle {
  parts := strings.Split(s, " ")
  id      := strings.Replace(parts[0], "#", "", -1)
  coordparts  := strings.Split(parts[2], ",")
  dimparts    := strings.Split(parts[3], "x")
  x, _ := strconv.Atoi(coordparts[0])
  y, _ := strconv.Atoi(strings.Replace(coordparts[1], ":", "", -1))
  w, _ := strconv.Atoi(dimparts[0])
  h, _ := strconv.Atoi(dimparts[1])
  return rectangle{overlap: false, id: id, x: x, y: y, w: w, h: h}
}

func get_overlap(rectangles []rectangle) int {
  buff := 0
  for _, r := range rectangles {
    for i := r.x; i < (r.x + r.w); i++ {
      for j := r.y; j < (r.y + r.h); j++ {
        pointmap[coordinate{x: i, y: j}] += 1
        if pointmap[coordinate{x: i, y: j}] == 2 {
          buff += 1
        }
      }
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
	seq := readLines("../data/input_3")
  rectangles := []rectangle{}
  for _, s := range seq {
    rectangles = append(rectangles, get_rectangle(s))
  }
  fmt.Printf("Q1: %d\n", get_overlap(rectangles))
  fmt.Printf("Q2: %s\n", get_no_overlap_id(rectangles))
}
