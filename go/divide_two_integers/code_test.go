package dividetwointegers

import "testing"

func TestDivide(t *testing.T) {
	tests := []struct {
		dividend int
		divisor  int
		expected int
	}{
		{3, 1, 3},
		{4, 2, 2},
		{58, 9, 6},
		{3749, 10, 374},
	}

	for _, test := range tests {
		result := divide(test.dividend, test.divisor)
		if result != test.expected {
			t.Errorf("divide(%d, %d) = %v; expected %v", test.dividend, test.divisor, result, test.expected)
		}
	}
}

func BenchmarkDivide(b *testing.B) {
	for b.Loop() {
		divide(2147483647, 1)
	}
}
