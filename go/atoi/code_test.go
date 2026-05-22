package atoi

import "testing"

func TestMyAtoi(t *testing.T) {
	tests := []struct {
		name string
		s    string
		want int
	}{
		{"test1", "42", 42},
		{"test2", "   -42", -42},
		{"test3", "4193 with words", 4193},
		{"test4", "words and 987", 0},
		{"test5", "-91283472332", -2147483648},
		{"test6", "9223372036854775808", 2147483647},
	}
	for _, tt := range tests {
		if got := myAtoi(tt.s); got != tt.want {
			t.Errorf("%s: myAtoi(%v) = %v, want %v", tt.name, tt.s, got, tt.want)
		}
	}
}

func BenchmarkAtoi(b *testing.B) {
	for b.Loop() {
		myAtoi("123456789")
	}
}
