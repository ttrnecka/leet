package valid_parentheses

import "testing"

func TestIsValid(t *testing.T) {
	tests := []struct {
		input    string
		expected bool
	}{
		{"()", true},
		{"(]", false},
		{"([)]", false},
		{"{[]}", true},
	}

	for _, test := range tests {
		result := isValid(test.input)
		if result != test.expected {
			t.Errorf("isValid(%q) = %v; expected %v", test.input, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		isValid("[][](){}")
	}
}
