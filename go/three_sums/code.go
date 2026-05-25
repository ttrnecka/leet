package three_sums

import "sort"

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	results := make([][]int, 0)

	for i := range nums {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		p1 := i + 1
		p2 := len(nums) - 1

		for p1 < p2 {
			total := nums[i] + nums[p1] + nums[p2]
			if total == 0 {
				results = append(results, []int{nums[i], nums[p1], nums[p2]})
				p1++
				p2--
				for p1 < p2 && nums[p1] == nums[p1-1] {
					p1 += 1
				}
			} else if total > 0 {
				p2--
			} else {
				p1++
			}
		}
	}
	return results
}
