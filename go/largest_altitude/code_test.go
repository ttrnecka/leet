package largestaltitude

import "testing"

func TestLargestAltitude(t *testing.T) {
	tests := []struct {
		gain     []int
		expected int
	}{
		{[]int{-4, -3, -2, -1, 4, 3, 2, 1}, 0},
		{[]int{1, 2, 3, 4, 5}, 15},
		{[]int{-1, -2, -3, -4, -5}, 0},
	}

	for _, test := range tests {
		result := largestAltitude(test.gain)
		if result != test.expected {
			t.Errorf("largestAltitude(%v) = %v; expected %v", test.gain, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		largestAltitude([]int{1, 2, 3, 4, 5})
	}
}
