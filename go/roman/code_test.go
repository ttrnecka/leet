package regexp

import "testing"

func TestIntToRoman(t *testing.T) {
	tests := []struct {
		input    int
		expected string
	}{
		{3, "III"},
		{4, "IV"},
		{58, "LVIII"},
		{3749, "MMMDCCXLIX"},
	}

	for _, test := range tests {
		result := intToRoman(test.input)
		if result != test.expected {
			t.Errorf("intToRoman(%d) = %v; expected %v", test.input, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		intToRoman(3759)
	}
}
