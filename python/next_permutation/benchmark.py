from next_permutation.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums):
        self.solution.nextPermutation(nums)

print(Benchmark().test([1, 2, 3]))
print(Benchmark().test([3, 2, 1]))