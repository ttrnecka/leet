from three_sums.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums):
        self.solution.threeSum(nums)

print(Benchmark().test([-1,0,1,2,-1,-4]))