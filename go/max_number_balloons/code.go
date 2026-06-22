package maxnumberballoons

import "math"

func maxNumberOfBalloons(text string) int {
	counter := map[byte]int{}

	for i := range len(text) {
		counter[text[i]]++
	}
	compareMap := map[byte]int{
		'b': 1,
		'a': 1,
		'l': 2,
		'o': 2,
		'n': 1,
	}

	max := float64(math.MaxInt32)
	for b, v := range compareMap {
		max = math.Min(float64(max), float64(counter[b]/v))
	}

	return int(max)
}
