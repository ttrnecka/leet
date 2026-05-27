from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left,right,s):
            if left == right and left+right == 2*n:
                res.append(s)
                return res
            
            if left < n:
                dfs(left+1,right,s+'(')

            if right < left:
                dfs(left,right+1,s+')')
        
        dfs(0,0,"")
        return res
if __name__ == "__main__":
    solution = Solution()

    print(solution.generateParenthesis(3)) # should print ["((()))","(()())","(())()","()(())","()()()"]