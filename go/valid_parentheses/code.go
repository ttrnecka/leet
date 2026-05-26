package valid_parentheses

func isValid(s string) bool {
	stack := make([]byte, 0)

	pmap := map[byte]byte{
		')': '(',
		']': '[',
		'}': '{',
	}
	for i := range len(s) {
		if _, ok := pmap[s[i]]; ok {
			if len(stack) == 0 {
				return false
			}
			popped := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if pmap[s[i]] != popped {
				return false
			}
		} else {
			stack = append(stack, s[i])
		}
	}
	return len(stack) == 0
}
