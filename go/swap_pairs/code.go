package swap_pairs

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func (ln *ListNode) Equal(ln2 *ListNode) bool {
	tmpln := ln
	for tmpln != nil || ln2 != nil {
		if tmpln == nil || ln2 == nil || tmpln.Val != ln2.Val {
			return false
		}
		tmpln = tmpln.Next
		ln2 = ln2.Next
	}
	return true
}

func (ln ListNode) String() string {
	s := ""
	tmp := &ln
	for tmp != nil {
		s = fmt.Sprintf("%s%d", s, tmp.Val)
		tmp = tmp.Next
	}
	return s
}

func swapPairs(head *ListNode) *ListNode {
	dummy := &ListNode{}
	dummy.Next = head
	current := dummy

	for current.Next != nil && current.Next.Next != nil {
		first := current.Next
		second := current.Next.Next

		first.Next = second.Next
		second.Next = first
		current.Next = second

		current = first
	}
	return dummy.Next
}
