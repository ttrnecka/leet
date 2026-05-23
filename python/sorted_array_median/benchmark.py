from sorted_array_median.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums1, nums2):
        self.solution.findMedianSortedArrays(nums1, nums2)

print(Benchmark().test([1,3,4,6,7,12,14,16,18], [2,4,7,8,12,15,17,19]))