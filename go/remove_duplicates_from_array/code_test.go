package removeduplicatesfromarray

import "testing"

func TestRemoveDuplicates(t *testing.T) {
	tests := []struct {
		nums         []int
		numsExpected []int
		expected     int
	}{
		{[]int{1, 1, 2}, []int{1, 2}, 2},
		{[]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}, []int{0, 1, 2, 3, 4}, 5},
		{[]int{}, []int{}, 0},
	}

	for _, test := range tests {
		result := removeDuplicates(test.nums)
		if result != test.expected {
			t.Errorf("removeDuplicates(%v) = %v; expected %v", test.nums, result, test.expected)
		}
		for i := 0; i < test.expected; i++ {
			if test.nums[i] != test.numsExpected[i] {
				t.Errorf("removeDuplicates(%v) modified array to %v; expected first %v elements to be %v", test.nums, test.nums, test.expected, test.numsExpected)
				break
			}
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		removeDuplicates([]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4})
	}
}
