package merge_k_sorted_lists

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

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	head := &ListNode{}
	dummy := head
	for list1 != nil || list2 != nil {
		if list1 != nil && list2 != nil && list1.Val < list2.Val || (list1 != nil && list2 == nil) {
			dummy.Next = list1
			list1 = list1.Next
		} else {
			dummy.Next = list2
			list2 = list2.Next
		}
		dummy = dummy.Next
	}
	return head.Next
}

func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}
	for len(lists) > 1 {
		var temp []*ListNode
		for i := 0; i < len(lists); i += 2 {
			l1 := lists[i]
			var l2 *ListNode
			if i+1 < len(lists) {
				l2 = lists[i+1]
			} else {
				l2 = nil
			}
			sorted := mergeTwoLists(l1, l2)
			temp = append(temp, sorted)
		}
		lists = temp
	}
	return lists[0]
}
