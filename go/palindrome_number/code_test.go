package palindrome_number

import "testing"

func TestIsPalindrome(t *testing.T) {
	tests := []struct {
		input    int
		expected bool
	}{
		{101, true},
		{10101, true},
		{1012, false},
		{-1012, false},
		{-121, false},
	}

	for _, test := range tests {
		result := isPalindrome(test.input)
		if result != test.expected {
			t.Errorf("isPalidrome(%d) = %v; expected %v", test.input, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		isPalindrome(10101010101)
	}
}
