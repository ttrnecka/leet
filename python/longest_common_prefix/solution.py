
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        while True:
            if i < len(strs[0]):
                char = strs[0][i]
            else:
                return prefix
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return prefix
            prefix += f"{char}"
            i+=1

        
        

if __name__ == "__main__":
    solution = Solution()

    # s = solution.addTwoNumbers(l1,l2)
    print(solution.longestCommonPrefix(["flower","flow","flight"])) # should print fl
    