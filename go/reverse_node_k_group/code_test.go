package reverse_node_k_group

import (
	"testing"
)

func TestReverseKGroup(t *testing.T) {
	tests := []struct {
		input    ListNode
		k        int
		expected ListNode
	}{
		{
			ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}},
			2,
			ListNode{Val: 2, Next: &ListNode{Val: 1, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3, Next: &ListNode{Val: 5}}}}},
		},
	}

	for _, test := range tests {
		result := reverseKGroup(&test.input, test.k)
		if !result.Equal(&test.expected) {
			// if result != &test.expected {
			t.Errorf("reverseKGroup(%s, %d) = %s; expected %s", test.input, test.k, result, test.expected)
		}
	}
}

func TestString(t *testing.T) {
	tests := []struct {
		input    ListNode
		expected string
	}{
		{ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3}}}, "123"},
	}
	for _, test := range tests {
		result := test.input.String()
		if result != test.expected {
			t.Errorf("String(%s) = %s; expected %s", test.input, result, test.expected)
		}
	}
}

func TestEqual(t *testing.T) {
	tests := []struct {
		a        ListNode
		b        ListNode
		expected bool
	}{
		{ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3}}}, ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3}}}, true},
		{ListNode{Val: 1, Next: &ListNode{Val: 2}}, ListNode{Val: 1, Next: &ListNode{Val: 3}}, false},
	}

	for _, test := range tests {
		result := test.a.Equal(&test.b)
		if result != test.expected {
			t.Errorf("Equal(%s, %s) = %t; expected %t", test.a, test.b, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		reverseKGroup(&ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}}, 2)
	}
}
