package removeelement

func removeElement(nums []int, val int) int {
	if len(nums) == 0 {
		return 0
	}
	ptr := 0
	for i := range nums {
		if nums[i] != val {
			if ptr != i {
				nums[ptr] = nums[i]
			}
			ptr++
		}
	}
	return ptr
}
