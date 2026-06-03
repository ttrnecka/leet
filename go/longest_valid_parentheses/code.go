package longestvalidparentheses

func longestValidParentheses(s string) int {
	max := 0
	dp := make([]int, len(s))

	for i := 1; i < len(s); i++ {
		if s[i] == ')' {
			if s[i-1] == '(' {
				dpt := 0
				if i >= 2 {
					dpt = dp[i-2]
				}
				dp[i] = dpt + 2
			} else if i-dp[i-1] > 0 && s[i-dp[i-1]-1] == '(' {
				dpt := 0
				if i-dp[i-1] >= 2 {
					dpt = dp[i-dp[i-1]-2]
				}
				dp[i] = dp[i-1] + dpt + 2
			}
			if max < dp[i] {
				max = dp[i]
			}
		}
	}
	return max
}
