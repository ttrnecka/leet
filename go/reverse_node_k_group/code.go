package reverse_node_k_group

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

func reverseKGroup(head *ListNode, k int) *ListNode {
	dummy := &ListNode{Next: head}
	groupPrev := dummy

	for {
		last := groupPrev
		for range k {
			last = last.Next
			if last == nil {
				return dummy.Next
			}
		}
		groupNext := last.Next

		prev, curr := groupNext, groupPrev.Next

		for curr != groupNext {
			new_node := curr.Next
			curr.Next = prev
			prev = curr
			curr = new_node
		}
		t := groupPrev.Next
		groupPrev.Next = last
		groupPrev = t

	}
}
