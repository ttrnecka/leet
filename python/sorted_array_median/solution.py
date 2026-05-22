from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        totalLength = len(nums1) + len(nums2)

        mid = totalLength // 2
        isOdd = totalLength % 2 == 1

        past = 0
        current = 0

        i = 0
        j = 0
        for _ in range(mid+1):
            past = current
            v1 = nums1[i] if i < len(nums1) else float('inf')
            v2 = nums2[j] if j < len(nums2) else float('inf')

            if v1 <= v2:
                i+=1
                current = v1
            else:
                j+=1
                current = v2

        if isOdd:
            return float(current)
        else:
            return float((past+current)/2)

if __name__ == "__main__":
    solution = Solution()

    print(solution.findMedianSortedArrays([1,2],[3,4,5])) # should print 2.5
    print(solution.findMedianSortedArrays([1,2],[3])) # should print 2