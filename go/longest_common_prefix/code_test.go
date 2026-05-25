package longestcommonprefix

import "testing"

func TestLongestCommonPrefix(t *testing.T) {
	tests := []struct {
		input    []string
		expected string
	}{
		{[]string{"aabf", "aab", "aabgh"}, "aab"},
		{[]string{"dog", "racecar", "car"}, ""},
		{[]string{"flower", "flow", "flight"}, "fl"},
	}

	for _, test := range tests {
		result := longestCommonPrefix(test.input)
		if result != test.expected {
			t.Errorf("intToRoman(%v) = %v; expected %v", test.input, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		longestCommonPrefix([]string{"aabf", "aab", "aabgh"})
	}
}
