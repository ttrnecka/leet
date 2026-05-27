package merge_k_sorted_lists

import (
	"testing"
)

func TestMergeKLists(t *testing.T) {
	tests := []struct {
		list1    *ListNode
		list2    *ListNode
		list3    *ListNode
		expected *ListNode
	}{
		{
			&ListNode{Val: 1},
			&ListNode{Val: 2, Next: &ListNode{Val: 3}},
			&ListNode{Val: 2},
			&ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3}}}},
		},
	}

	for _, test := range tests {
		result := mergeKLists([]*ListNode{test.list1, test.list2, test.list3})
		if !result.Equal(test.expected) {
			// if result != &test.expected {
			t.Errorf("mergeKLists(%s, %s, %s) = %s; expected %s", test.list1, test.list2, test.list3, result, test.expected)
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
		l1, l2, l3 := getLists()
		mergeKLists([]*ListNode{&l1, &l2, &l3})
	}
}

func getLists() (ListNode, ListNode, ListNode) {
	l1 := ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}}
	l2 := ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}
	l3 := ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}
	return l1, l2, l3
}
