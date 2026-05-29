package needleinhaystack

import "testing"

func TestStrStr(t *testing.T) {
	tests := []struct {
		haystack string
		needle   string
		expected int
	}{
		{"sadbutsad", "sad", 0},
		{"leetcode", "leeto", -1},
	}

	for _, test := range tests {
		result := strStr(test.haystack, test.needle)
		if result != test.expected {
			t.Errorf("strStr(%q, %q) = %v; expected %v", test.haystack, test.needle, result, test.expected)
		}
	}
}

func BenchmarkStrStr(b *testing.B) {
	for b.Loop() {
		strStr("sasdbutsad", "sad")
	}
}
