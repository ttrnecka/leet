from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        ptr=0
        for i in range(len(nums)):
            if nums[i] != val:
                if i != ptr:
                    nums[ptr]=nums[i]
                ptr+=1
        return ptr
        

if __name__ == "__main__":
    solution = Solution()
    num = [1,1,2]
    print(solution.removeElement(num,1),num)
    num = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeElement(num,1),num)