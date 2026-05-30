package nextpermutation

func rev(nums []int) {
	start := 0
	end := len(nums) - 1
	for start < end {
		nums[start], nums[end] = nums[end], nums[start]
		start++
		end--
	}
}

func nextPermutation(nums []int) {

	l := len(nums)
	idx := -1
	for i := l - 1; i > 0; i-- {
		if nums[i-1] < nums[i] {
			idx = i
			break
		}
	}

	// reverse whole
	if idx == -1 {
		rev(nums)
		return
	}

	rev(nums[idx:])

	swapIdx := -1
	// find j in subarray that is higher than i-i
	for j := idx; j < len(nums); j++ {
		if nums[j] > nums[idx-1] {
			swapIdx = j
			break
		}
	}

	nums[idx-1], nums[swapIdx] = nums[swapIdx], nums[idx-1]
}
