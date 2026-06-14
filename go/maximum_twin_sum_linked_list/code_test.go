package maximumtwinsumlinkedlist

import "testing"

func TestPairSum(t *testing.T) {
	tests := []struct {
		head     *ListNode
		expected int
	}{
		{&ListNode{Val: 5, Next: &ListNode{Val: 4, Next: &ListNode{Val: 2, Next: &ListNode{Val: 1}}}}, 6},
		{&ListNode{Val: 4, Next: &ListNode{Val: 2, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3}}}}, 7},
		{&ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4}}}}, 5},
	}

	for _, test := range tests {
		result := pairSum(test.head)
		if result != test.expected {
			t.Errorf("pairSum(%v) = %v; expected %v", test.head, result, test.expected)
		}
	}
}

func BenchmarkPairSum(b *testing.B) {
	for b.Loop() {
		head := &ListNode{Val: 5, Next: &ListNode{Val: 4, Next: &ListNode{Val: 2, Next: &ListNode{Val: 1}}}}
		pairSum(head)
	}
}
