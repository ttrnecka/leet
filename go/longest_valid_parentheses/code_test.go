package longestvalidparentheses

import "testing"

func TestLongestValidParentheses(t *testing.T) {
	tests := []struct {
		input    string
		expected int
	}{
		{")()())", 4},
		{"(()", 2},
		{"()(())", 6},
	}

	for _, test := range tests {
		result := longestValidParentheses(test.input)
		if result != test.expected {
			t.Errorf("longestValidParentheses(%v) = %v; expected %v", test.input, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		longestValidParentheses(")()())")
	}
}
