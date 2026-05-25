
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()
        ans = set()
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    last = target-nums[i]-nums[j]-nums[k]
                    if last in seen:
                        arr = sorted([nums[i],nums[j],nums[k],last])
                        ans.add((arr[0],arr[1],arr[2],arr[3]))        
            seen.add(nums[i])

        return ans
    
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            # skip duplicate starting values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums) - 2):
                # skip duplicate starting values
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1

                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print(solution.fourSum([2, 2, 2, 2, 2], 8))