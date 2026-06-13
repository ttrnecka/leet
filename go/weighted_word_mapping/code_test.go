package weighted_word_mapping

import "testing"

func TestMapWordWeights(t *testing.T) {
	tests := []struct {
		words    []string
		weights  []int
		expected string
	}{
		{[]string{"abcd", "def", "xyz"}, []int{5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2}, "rij"},
		{[]string{"a", "b", "c"}, []int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, "yyy"},
		{[]string{"abcd"}, []int{7, 5, 3, 4, 3, 5, 4, 9, 4, 2, 2, 7, 10, 2, 5, 10, 6, 1, 2, 2, 4, 1, 3, 4, 4, 5}, "g"},
	}

	for _, test := range tests {
		result := mapWordWeights(test.words, test.weights)
		if result != test.expected {
			t.Errorf("mapWordWeights(%q, %q) = %v; expected %v", test.words, test.weights, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		mapWordWeights([]string{"aaaaaabba"}, []int{1, 2, 3})
	}
}
