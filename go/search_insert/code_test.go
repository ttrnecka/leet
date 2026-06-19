package searchinsert

import "testing"

func TestSearchInsert(t *testing.T) {
	tests := []struct {
		nums     []int
		target   int
		expected int
	}{
		{[]int{1, 3, 5, 6}, 5, 2},
		{[]int{1, 2, 3, 4, 5}, 15, 5},
		{[]int{1, 3, 5, 6}, 2, 1},
	}

	for _, test := range tests {
		result := searchInsert(test.nums, test.target)
		if result != test.expected {
			t.Errorf("searchInsert(%v, %v) = %v; expected %v", test.nums, test.target, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		searchInsert([]int{1, 2, 3, 4, 5}, 3)
	}
}
