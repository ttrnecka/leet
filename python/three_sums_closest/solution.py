
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        closest_sum = (sorted_nums[0]+sorted_nums[1]+sorted_nums[2])
        main_diff = abs(target - closest_sum)
        i =0 
        while i < len(sorted_nums)-2:
            p1 = i+1
            p2 = len(sorted_nums)-1
            while p1 < p2:
                sum = (sorted_nums[i] + sorted_nums[p1] + sorted_nums[p2])
                diff = abs(target - sum)
                if diff < main_diff:
                    main_diff = diff
                    closest_sum = sum
                elif sum < target:
                    p1+=1
                elif sum > target:
                    p2-=1
                else:
                    return sum
            i+=1
            while i< len(sorted_nums) and sorted_nums[i-1] == sorted_nums[i]:
                i+=1
            
        return closest_sum
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-1,2,1,-4]))  # Output 2