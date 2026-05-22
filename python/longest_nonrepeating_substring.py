
from typing import Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        max = 0
        for end,char in enumerate(s):
            # found=last_seen.get(s[end],None)
            if char in last_seen and last_seen[char] + 1 > start:
                start = last_seen[char] + 1
            if end - start + 1 > max:
                max = end - start + 1
            last_seen[char] = end

        return max
        

if __name__ == "__main__":
    solution = Solution()

    # s = solution.addTwoNumbers(l1,l2)
    print(solution.lengthOfLongestSubstring("acbdaseeedddea")) # should print 5
    