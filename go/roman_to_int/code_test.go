package regexp

import "testing"

func TestRomanToInt(t *testing.T) {
	tests := []struct {
		input    string
		expected int
	}{
		{"III", 3},
		{"IV", 4},
		{"LVIII", 58},
		{"MMMDCCXLIX", 3749},
	}

	for _, test := range tests {
		result := romanToInt(test.input)
		if result != test.expected {
			t.Errorf("romanToInt(%s) = %d; expected %d", test.input, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		romanToInt("MMMDCCXLIX")
	}
}
