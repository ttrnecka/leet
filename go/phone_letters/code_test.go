package phone_letters

import "testing"

func TestLetterCombinations(t *testing.T) {
	tests := []struct {
		input    string
		expected []string
	}{
		{"23", []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}},
		{"2", []string{"a", "b", "c"}},
		{"", []string{}},
	}

	for _, test := range tests {
		result := letterCombinations(test.input)
		if len(result) != len(test.expected) {
			t.Errorf("letterCombinations(%v) = %v; expected %v", test.input, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		letterCombinations("23")
	}
}
