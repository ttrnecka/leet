package removeduplicatesfromarray

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	uniqP := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[uniqP] {
			uniqP++
			nums[uniqP] = nums[i]
		}
	}
	return uniqP + 1
}
