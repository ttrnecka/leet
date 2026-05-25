package four_sums

import "testing"

func TestFourSum(t *testing.T) {
	tests := []struct {
		input    []int
		target   int
		expected [][]int
	}{
		{[]int{1, 0, -1, 0, -2, 2}, 0, [][]int{{-2, -1, 1, 2}, {-2, 0, 0, 2}, {-1, 0, 0, 1}}},
		{[]int{2, 2, 2, 2, 2}, 8, [][]int{{2, 2, 2, 2}}},
	}

	for _, test := range tests {
		result := fourSum(test.input, test.target)
		if len(result) != len(test.expected) {
			t.Errorf("fourSum(%v, %v) = %v; expected %v", test.input, test.target, result, test.expected)
		}
		for i := range result {
			if len(result[i]) != len(test.expected[i]) {
				t.Errorf("fourSum(%v, %v) = %v; expected %v", test.input, test.target, result, test.expected)
			}
			for j := range result[i] {
				if result[i][j] != test.expected[i][j] {
					t.Errorf("fourSum(%v, %v) = %v; expected %v", test.input, test.target, result, test.expected)
				}
			}
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		fourSum([]int{1, 0, -1, 0, -2, 2}, 0)
	}
}
