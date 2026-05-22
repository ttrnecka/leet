package regexp

import "testing"

func TestIsMatch(t *testing.T) {
	tests := []struct {
		input    string
		pattern  string
		expected bool
	}{
		{"aaa", "a*a", true},
		{"aba", "a*a", false},
		{"aab", "c*a*b", true},
		{"ab", "a*", false},
		{"aa", "a", false},
	}

	for _, test := range tests {
		result := isMatch(test.input, test.pattern)
		if result != test.expected {
			t.Errorf("isMatch(%q, %q) = %v; expected %v", test.input, test.pattern, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		isMatch("aaaaaabba", "a*ba")
	}
}
