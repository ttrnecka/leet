package create_binary_tree_from_description

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func (tn *TreeNode) Equal(tn2 *TreeNode) bool {

	if tn == nil && tn2 == nil {
		return true
	}
	if tn == nil || tn2 == nil || tn.Val != tn2.Val {
		return false
	}
	if !tn.Left.Equal(tn2.Left) || !tn.Right.Equal(tn2.Right) {
		return false
	}
	return true
}

func createBinaryTree(descriptions [][]int) *TreeNode {
	nodes := make(map[int]*TreeNode)
	root := 0

	for _, node_desc := range descriptions {
		parent := node_desc[0]
		child := node_desc[1]
		isLeft := node_desc[2]

		_, ok := nodes[parent]
		if !ok {
			nodes[parent] = &TreeNode{Val: parent}
			root ^= parent
		}
		_, ok = nodes[child]
		if !ok {
			nodes[child] = &TreeNode{Val: child}
			root ^= child
		}
		if isLeft == 1 {
			nodes[parent].Left = nodes[child]
		} else {
			nodes[parent].Right = nodes[child]
		}
		root ^= child
	}

	return nodes[root]
}

func PrintTree(root *TreeNode) {
	printTree(root, "", true)
}

func printTree(node *TreeNode, prefix string, isTail bool) {
	if node == nil {
		return
	}

	if node.Right != nil {
		newPrefix := prefix
		if isTail {
			newPrefix += "│   "
		} else {
			newPrefix += "    "
		}
		printTree(node.Right, newPrefix, false)
	}

	fmt.Printf("%s", prefix)
	if isTail {
		fmt.Print("└── ")
	} else {
		fmt.Print("┌── ")
	}
	fmt.Println(node.Val)

	if node.Left != nil {
		newPrefix := prefix
		if isTail {
			newPrefix += "    "
		} else {
			newPrefix += "│   "
		}
		printTree(node.Left, newPrefix, true)
	}
}
