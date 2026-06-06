package search_in_rotated_sorted_array

import "testing"

func TestSearch(t *testing.T) {
	tests := []struct {
		nums     []int
		target   int
		expected int
	}{
		{[]int{4, 5, 6, 7, 0, 1, 2}, 0, 4},
		{[]int{4, 5, 6, 7, 0, 1, 2}, 3, -1},
		{[]int{1}, 0, -1},
	}

	for _, test := range tests {
		result := search(test.nums, test.target)
		if result != test.expected {
			t.Errorf("search(%v, %d) = %d; expected %d", test.nums, test.target, result, test.expected)
		}
	}
}

func BenchmarkSearch(b *testing.B) {
	for b.Loop() {
		search([]int{4, 5, 6, 7, 0, 1, 2}, 0)
	}
}
