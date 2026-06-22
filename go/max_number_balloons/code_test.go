package maxnumberballoons

import "testing"

func TestMaxNumberOfBalloons(t *testing.T) {
	tests := []struct {
		input    string
		expected int
	}{
		{"nlaebolko", 1},
		{"loonbalxballpoon", 2},
		{"leetcode", 0},
	}

	for _, test := range tests {
		result := maxNumberOfBalloons(test.input)
		if result != test.expected {
			t.Errorf("maxNumberOfBalloons(%q) = %v; expected %v", test.input, result, test.expected)
		}
	}
}

func BenchmarkMaxNumberOfBalloons(b *testing.B) {
	for b.Loop() {
		maxNumberOfBalloons("aaaaaabba")
	}
}
