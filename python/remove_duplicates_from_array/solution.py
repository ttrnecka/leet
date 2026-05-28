from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        uniqP = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[uniqP]:
                uniqP+=1
                nums[uniqP] = nums[i]
        return uniqP+1

if __name__ == "__main__":
    solution = Solution()
    num = [1,1,2]
    print(solution.removeDuplicates(num),num)
    num = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(num),num)