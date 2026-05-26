package remove_nth_node

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func (ln *ListNode) Equal(ln2 *ListNode) bool {
	tmpln := ln
	for tmpln != nil && ln2 != nil {
		if tmpln.Val != ln2.Val {
			return false
		}
		tmpln = tmpln.Next
		ln2 = ln.Next
	}
	if tmpln == nil && ln2 == nil {
		return true
	}
	return false
}

func (ln *ListNode) String() string {
	s := ""
	tmp := ln
	for tmp != nil {
		s = fmt.Sprintf("%s%d", s, tmp.Val)
		tmp = tmp.Next
	}
	return s
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	fast, slow := head, head

	for range n {
		fast = fast.Next
	}
	// removing first node
	if fast == nil {
		return head.Next
	}

	for fast.Next != nil {
		fast = fast.Next
		slow = slow.Next
	}

	slow.Next = slow.Next.Next

	return head
}
