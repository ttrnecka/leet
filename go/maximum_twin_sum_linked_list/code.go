package maximumtwinsumlinkedlist

type ListNode struct {
	Val  int
	Next *ListNode
}

func pairSum(head *ListNode) int {
	slow := head
	fast := head
	var prev *ListNode

	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next

		next := slow.Next
		slow.Next = prev
		prev = slow
		slow = next
	}

	res := 0
	for slow != nil {
		if slow.Val+prev.Val > res {
			res = slow.Val + prev.Val
		}
		slow = slow.Next
		prev = prev.Next
	}
	return res
}
