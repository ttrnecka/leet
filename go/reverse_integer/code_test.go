package reverse_integer

import "testing"

func TestReverse(t *testing.T) {
	tests := []struct {
		input    int
		expected int
	}{
		{123, 321},
		{-123, -321},
		{120, 21},
		{0, 0},
	}

	for _, test := range tests {
		result := reverse(test.input)
		if result != test.expected {
			t.Errorf("reverse(%d) = %d; expected %d", test.input, result, test.expected)
		}
	}
}

func BenchmarkReverse(b *testing.B) {
	for b.Loop() {
		reverse(123456789)
	}
}
