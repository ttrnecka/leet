package reverse_integer


import "math"

func reverse(x int) int {
	result := 0
	for x != 0 {
		remainder := x % 10
		x = x / 10
		result = 10*result + remainder
		if result > math.MaxInt32 || result < math.MinInt32 {
			return 0
		}
	}
	return result
}
