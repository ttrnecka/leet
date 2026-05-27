from swap_pair.solution import Solution, createList
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums):
        l =  createList(nums)
        self.solution.swapPairs(l)

print(Benchmark().test([1,2,3,4,5]))