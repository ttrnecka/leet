from four_sums.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums):
        self.solution.fourSum(nums, 0)
    @benchmark(repeats=100)
    def test2(self, nums):
        self.solution.fourSum2(nums, 0)

print(Benchmark().test([1, 0, -1, 0, -2, 2]))
print(Benchmark().test2([1, 0, -1, 0, -2, 2]))