from typing import List

class Solution:
    def bin_search(self,nums: List[int], target: int, shift: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        if len(nums) == 0:
            return -1
        mid = len(nums) // 2
        if nums[mid] == target:
            return shift + mid
        if nums[mid] < target:
            nums=nums[mid:]
            diff = mid
        else:
            nums=nums[0:mid]
            diff = 0
        return self.bin_search(nums,target,shift+diff)

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        if nums[0] <= nums[mid] and nums[0] <= target <= nums[mid]:
            return self.bin_search(nums[0:mid],target,0)
        if nums[mid] <= nums[-1] and nums[mid] <= target <= nums[-1]:
            return self.bin_search(nums[mid:],target,mid)
        if nums[0] > nums[mid] and not (nums[0] <= target <= nums[mid]):
            return self.search(nums[0:mid],target)
        if nums[mid] > nums[-1] and not (nums[mid] <= target <= nums[-1]):
            pos = self.search(nums[mid:],target)
            return -1 if pos == -1 else mid+pos
        return -1
        

        
if __name__ == "__main__":
    solution = Solution()
    # print(solution.bin_search([0,1,2,3,4,5,6,7], 8,0))
    # print(solution.search([4,5,6,7,0,1,2], 0))
    # print(solution.search([4,5,6,7,0,1,2], 3))
    # print(solution.search([1,3], 3))
    # print(solution.search([3,5,1], 1))
    # print(solution.search([1], 1))
    print(solution.search([4,5,6,7,0,1,2], 6))