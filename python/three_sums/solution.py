
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        results = []
        i =0 
        while i < len(sorted_nums)-2:
            p1 = i+1
            p2 = len(sorted_nums)-1
            while p1 < p2:
                sum = sorted_nums[i] + sorted_nums[p1] + sorted_nums[p2]
                if sum == 0:
                    results.append([sorted_nums[i],sorted_nums[p1],sorted_nums[p2]])
                    p1+=1
                    p2-=1
                    while p1 < p2 and sorted_nums[p1] == sorted_nums[p1-1]:
                        p1+=1
                elif sum > 0:
                    p2-=1
                else:
                    p1+=1
            i+=1
            while i< len(sorted_nums) and sorted_nums[i-1] == sorted_nums[i]:
                i+=1
            
        return results
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, 0, 1], [-1, -1, 2]]