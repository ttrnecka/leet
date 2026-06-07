package create_binary_tree_from_description

import "testing"

func TestCreateBinaryTree(t *testing.T) {
	tests := []struct {
		descriptions [][]int
		expected     *TreeNode
	}{
		{[][]int{{20, 15, 1}, {20, 17, 0}, {50, 20, 1}, {50, 80, 0}, {80, 19, 1}}, expectedTree1()},
	}

	for _, test := range tests {
		result := createBinaryTree(test.descriptions)
		if result.Equal(test.expected) != true {
			t.Errorf("createBinaryTree(%v) = %v; expected %v", test.descriptions, result, test.expected)
			PrintTree(result)
			PrintTree(test.expected)
		}
	}
}

func TestEqual(t *testing.T) {
	tests := []struct {
		a        *TreeNode
		b        *TreeNode
		expected bool
	}{
		{&TreeNode{Val: 50}, &TreeNode{Val: 50}, true},
		{&TreeNode{Val: 50}, &TreeNode{Val: 51}, false},
		{&TreeNode{Val: 50, Left: &TreeNode{Val: 20}}, &TreeNode{Val: 50}, false},
		{&TreeNode{Val: 50, Left: &TreeNode{Val: 20}}, &TreeNode{Val: 50, Left: &TreeNode{Val: 20}}, true},
	}

	for _, test := range tests {
		result := test.a.Equal(test.b)
		if result != test.expected {
			t.Errorf("Equal(%v, %v) = %v; expected %v", test.a, test.b, result, test.expected)
		}
	}
}

func expectedTree1() *TreeNode {
	root := &TreeNode{Val: 50}
	root.Left = &TreeNode{Val: 20}
	root.Right = &TreeNode{Val: 80}
	root.Left.Left = &TreeNode{Val: 15}
	root.Left.Right = &TreeNode{Val: 17}
	root.Right.Left = &TreeNode{Val: 19}
	return root
}
func BenchmarkCreateBinaryTree(b *testing.B) {
	for b.Loop() {
		createBinaryTree([][]int{{20, 15, 1}, {20, 17, 0}, {50, 20, 1}, {50, 80, 0}, {80, 19, 0}})
	}
}
