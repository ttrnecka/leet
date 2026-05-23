package regexp

import "testing"

func TestMaxArea(t *testing.T) {
	tests := []struct {
		input    []int
		expected int
	}{
		{[]int{1, 8, 6, 2, 5, 4, 8, 3, 7}, 49},
		{[]int{1, 1}, 1},
	}

	for _, test := range tests {
		result := maxArea(test.input)
		if result != test.expected {
			t.Errorf("maxArea(%q) = %q; expected %q", test.input, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7})
	}
}
