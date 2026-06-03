class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max = 0
        dp = [0] * len(s)

        for i in range(1,len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = (dp[i-2] if i >=2 else 0) + 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if (i-dp[i-1]>=2) else 0) + 2
                if dp[i] > max:
                    max = dp[i]
        return max

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses(")()())")) # should print 4