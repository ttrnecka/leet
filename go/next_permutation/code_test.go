package nextpermutation

import (
	"slices"
	"testing"
)

func TestNextPermutation(t *testing.T) {
	tests := []struct {
		input    []int
		expected []int
	}{
		{[]int{1, 2, 3}, []int{1, 3, 2}},
		{[]int{3, 2, 1}, []int{1, 2, 3}},
		{[]int{1, 1, 5}, []int{1, 5, 1}},
	}

	for _, test := range tests {
		nextPermutation(test.input)
		if !slices.Equal(test.input, test.expected) {
			t.Errorf("nextPermutation(%v) = %v; expected %v", test.input, test.input, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		nextPermutation([]int{1, 2, 3})
	}
}
