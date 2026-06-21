from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        say = "1"

        for c in range(1, n):
            say = self.rle(say)
        return say

    def rle(self, s: str) -> str:
        rle_str = ""

        if len(s) == 0:
            return ""

        val = s[0]
        cnt = 1
        for c in s[1:]:
            if c == val:
                cnt+=1
            else:
                rle_str += f"{cnt}{val}"
                val = c
                cnt = 1
        rle_str += f"{cnt}{val}"
        return rle_str
        
        
if __name__ == "__main__":
    solution = Solution()

    print(solution.countAndSay(1)) # should print "1"
    print(solution.countAndSay(2)) # should print "11"
    print(solution.countAndSay(3)) # should print "21"
    print(solution.countAndSay(4)) # should print "1211"