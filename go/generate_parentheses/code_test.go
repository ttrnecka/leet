package generate_parentheses

import (
	"slices"
	"testing"
)

func TestGenerateParenthesis(t *testing.T) {
	tests := []struct {
		input    int
		expected []string
	}{
		{3, []string{"((()))", "(()())", "(())()", "()(())", "()()()"}},
	}

	for _, test := range tests {
		result := generateParenthesis(test.input)
		if !slices.Equal(result, test.expected) {
			t.Errorf("generateParenthesis(%d) = %v; expected %v", test.input, result, test.expected)
		}
	}
}

func BenchmarkGenerateParenthesis(b *testing.B) {
	for b.Loop() {
		generateParenthesis(3)
	}
}
