package substring_with_concatenation_of_all_words

import (
	"slices"
	"testing"
)

func TestFindSubstring(t *testing.T) {
	tests := []struct {
		s        string
		words    []string
		expected []int
	}{
		{"barfoothefoobarman", []string{"foo", "bar"}, []int{0, 9}},
	}

	for _, test := range tests {
		result := findSubstring(test.s, test.words)
		if !slices.Equal(result, test.expected) {
			t.Errorf("findSubstring(%q, %v) = %v; expected %v", test.s, test.words, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		findSubstring("barfoothefoobarman", []string{"foo", "bar"})
	}
}

func BenchmarkConvert2(b *testing.B) {
	for b.Loop() {
		findSubstring2("barfoothefoobarman", []string{"foo", "bar"})
	}
}
