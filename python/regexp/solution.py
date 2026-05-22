import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m , n = len(s), len(p)
        d = [[False] * (n+1) for _ in range(m+1) ]
        # emty string matches empty pattern
        d[0][0] = True

        for j in range(2,n+1):
            if p[j-1] == '*':
                d[0][j] = d[0][j-2]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == '*':
                              # zero matches of previous character 
                              # or matches previous character
                    d[i][j] = d[i][j-2] or (d[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                else:
                    d[i][j] = d[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        return d[m][n]
if __name__ == "__main__":
    solution = Solution()

    print(solution.isMatch("aa", "a.")) # should print True
    print(solution.isMatch("ab", "a.")) # should print True
    print(solution.isMatch("ab", "a*")) # should print False
    print(solution.isMatch("ab", ".*")) # should print True