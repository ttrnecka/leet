package generate_parentheses

func generateParenthesis(n int) []string {
	result := make([]string, 0)
	path := make([]byte, 0, 2*n)

	var dfs func(left, right int)

	dfs = func(left, right int) {
		if len(path) == 2*n {
			result = append(result, string(path))
			return
		}

		if left < n {
			path = append(path, '(')
			dfs(left+1, right)
			path = path[:len(path)-1] // backtrack
		}

		if right < left {
			path = append(path, ')')
			dfs(left, right+1)
			path = path[:len(path)-1] // backtrack
		}
	}

	dfs(0, 0)
	return result
}
