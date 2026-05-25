package three_sums_closest

import "testing"

func TestThreeSumClosest(t *testing.T) {
	tests := []struct {
		input    []int
		target   int
		expected int
	}{
		{[]int{-1, 2, 1, -4}, 1, 2},
		{[]int{0, 0, 0}, 1, 0},
		{[]int{4, 0, 5, -5, 3, 3, 0, -4, -5}, -2, -2},
		{[]int{10, 20, 30, 40, 50, 60, 70, 80, 90}, 1, 60},
	}

	for _, test := range tests {
		result := threeSumClosest(test.input, test.target)
		if result != test.expected {
			t.Errorf("threeSumClosest(%v, %v) = %v; expected %v", test.input, test.target, result, test.expected)
		}
	}
}

func BenchmarkThreeSumClosest(b *testing.B) {
	for b.Loop() {
		threeSumClosest([]int{-1, 0, 1, 2, -1, -4}, 1)
	}
}
