package three_sums

import "testing"

func TestThreeSum(t *testing.T) {
	tests := []struct {
		input    []int
		expected [][]int
	}{
		{[]int{-1, 0, 1, 2, -1, -4}, [][]int{{-1, -1, 2}, {-1, 0, 1}}},
		{[]int{0, 1, 1}, [][]int{}},
		{[]int{-2, 0, 1, 1, 2}, [][]int{[]int{-2, 0, 2}, []int{-2, 1, 1}}},
	}

	for _, test := range tests {
		result := threeSum(test.input)
		if len(result) != len(test.expected) {
			t.Errorf("threeSum(%v) = %v; expected %v", test.input, result, test.expected)
		}
		for i := range result {
			if len(result[i]) != len(test.expected[i]) {
				t.Errorf("threeSum(%v) = %v; expected %v", test.input, result, test.expected)
			}
			for j := range result[i] {
				if result[i][j] != test.expected[i][j] {
					t.Errorf("threeSum(%v) = %v; expected %v", test.input, result, test.expected)
				}
			}
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		threeSum([]int{-1, 0, 1, 2, -1, -4})
	}
}
