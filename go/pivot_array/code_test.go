package pivot_array

import "testing"

func TestPivotArray(t *testing.T) {
	tests := []struct {
		input    []int
		pivot    int
		expected []int
	}{
		{[]int{1, 0, -1, 0, -2, 2}, 0, []int{-1, -2, 0, 0, 1, 2}},
		{[]int{2, 2, 2, 2, 2}, 8, []int{2, 2, 2, 2, 2}},
		{[]int{9, 12, 5, 10, 14, 3, 10}, 10, []int{9, 5, 3, 10, 10, 12, 14}},
	}

	for _, test := range tests {
		result := pivotArray(test.input, test.pivot)
		if len(result) != len(test.expected) {
			t.Errorf("pivotArray(%v, %v) = %v; expected %v", test.input, test.pivot, result, test.expected)
		}
		for i := range result {
			if result[i] != test.expected[i] {
				t.Errorf("pivotArray(%v, %v) = %v; expected %v", test.input, test.pivot, result, test.expected)
			}
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		pivotArray([]int{1, 0, -1, 0, -2, 2}, 0)
	}
}
