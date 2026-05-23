import re
from typing import List

class Solution:
    def maxAreaNaive(self, height: List[int]) -> int:
        max = 0
        for i in range(0,len(height)):
            for j in range(i+1,len(height)):
                amount = (j-i)*min(height[i],height[j])
                if amount > max:
                    max = amount
        return max

    def maxArea(self, height: List[int]) -> int:
        max, left, right = 0, 0, len(height)-1
        while left < right:
            amount = (right-left)*min(height[left],height[right])
            if amount > max:
                max = amount
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max

if __name__ == "__main__":
    solution = Solution()

    print(solution.maxAreaNaive([1,8,6,2,5,4,8,3,7])) # should print 49