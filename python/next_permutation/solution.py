from typing import List
class Solution:
    def rev(self,nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1

    def nextPermutation(self, nums: List[int]) -> None:
        
        idx = -1
        l = len(nums)

        for i in range(l-2,-1,-1):
            if nums[i] < nums[i+1]:
                idx = i
                break

        if idx == -1:
            self.rev(nums,0,l-1)
            return
        
        self.rev(nums,idx+1,l-1)

        swapIdx = -1
        
        for j in range(idx+1,l):
            if nums[j] > nums[idx]:
                swapIdx = j
                break

        nums[swapIdx], nums[idx] = nums[idx], nums[swapIdx]
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.nextPermutation([1, 2, 3])) # should print [1, 3, 2]