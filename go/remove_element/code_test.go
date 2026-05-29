package removeelement

import "testing"

func TestRemoveDuplicates(t *testing.T) {
	tests := []struct {
		nums         []int
		val          int
		numsExpected []int
		expected     int
	}{
		{[]int{1, 1, 2}, 1, []int{2}, 1},
		{[]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}, 1, []int{0, 0, 2, 2, 3, 3, 4}, 7},
		{[]int{}, 1, []int{}, 0},
	}

	for _, test := range tests {
		result := removeElement(test.nums, test.val) // Assuming we want to remove all occurrences of 1
		if result != test.expected {
			t.Errorf("removeElement(%v, %v) = %v; expected %v", test.nums, test.val, result, test.expected)
		}
		for i := 0; i < test.expected; i++ {
			if test.nums[i] != test.numsExpected[i] {
				t.Errorf("removeElement(%v, %v) modified array to %v; expected first %v elements to be %v", test.nums, test.val, test.nums, test.expected, test.numsExpected)
				break
			}
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		removeElement([]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}, 1)
	}
}
