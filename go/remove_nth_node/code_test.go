package remove_nth_node

import (
	"testing"
)

func TestRemoveNthNode(t *testing.T) {
	tests := []struct {
		input    ListNode
		n        int
		expected ListNode
	}{
		{ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}}, 2, ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 5}}}}},
	}

	for _, test := range tests {
		result := removeNthFromEnd(&test.input, test.n)
		if !result.Equal(&test.expected) {
			// if result != &test.expected {
			t.Errorf("removeNthFromEnd(%s, %d) = %s; expected %s", test.input, test.n, result, test.expected)
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
		removeNthFromEnd(&ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}}, 2)
	}
}
