package three_sums_closest

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	closest_sum := math.MaxInt
	min_diff := math.MaxFloat64
	n := len(nums)
	for i := range n - 2 {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		left := i + 1
		right := n - 1
		for left < right {
			current_sum := nums[i] + nums[left] + nums[right]
			diff := math.Abs(float64(target - current_sum))

			if diff < min_diff {
				min_diff = diff
				closest_sum = current_sum
			} else if current_sum > target {
				right--
			} else if current_sum < target {
				left++
			} else {
				return current_sum
			}
		}
	}
	return closest_sum
}
