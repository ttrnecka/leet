package regexp

import "math"

func maxArea(height []int) int {
	max := 0
	left, right := 0, len(height)-1

	for left < right {
		amount := (right - left) * int(math.Min(float64(height[left]), float64(height[right])))
		if amount > max {
			max = amount
		}
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}
	return max
}
