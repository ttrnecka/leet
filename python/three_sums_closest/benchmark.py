from three_sums_closest.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums,target):
        self.solution.threeSumClosest(nums,target)

print(Benchmark().test([-1,2,1,-4],1))