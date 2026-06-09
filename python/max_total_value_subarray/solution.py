from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minG = maxG = nums[0]

        for v in nums:
            if v < minG:
                minG = v
            if v > maxG:
                maxG = v

        return (maxG-minG) * k