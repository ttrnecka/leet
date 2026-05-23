from two_sums.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums, target):
        self.solution.twoSum(nums, target)

print(Benchmark().test([11,2, 15, 11, 7], 9))