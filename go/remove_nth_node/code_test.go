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
			t.Errorf("removeNthFromEnd(%#v, %d) = %#v; expected %#v", test.input, test.n, result, test.expected)
		}
	}
}

func BenchmarkConvert(b *testing.B) {
	for b.Loop() {
		removeNthFromEnd(&ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}}, 2)
	}
}
